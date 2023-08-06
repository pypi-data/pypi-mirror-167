import os
import sys
import subprocess
from tempfile import NamedTemporaryFile
from typing import Optional
from unittest.mock import patch, MagicMock
from contextlib import ExitStack, contextmanager

import pytest
from ..client.base import SlurmBaseApi
from ..client.script import SlurmScriptApi
from ..client.pyscript import SlurmPythonJobApi
from ..client.errors import SlurmError


@contextmanager
def mock_slurm_clients(tmpdir):
    last_job_id = 0
    jobs = dict()

    def _get(
        path: str,
        request_options=None,
        error_msg: Optional[str] = None,
        raise_on_error: bool = True,
    ):
        if path == "/openapi":
            return {"info": {"version": SlurmBaseApi.VERSION}}
        elif path.startswith("/slurm/v0.0.37/job/"):
            job_id = int(path.split("/")[-1])
            job_info = jobs.get(job_id)
            if job_info is None:
                if raise_on_error:
                    raise SlurmError(error_msg)
                else:
                    return dict()
            return {"jobs": [job_info]}
        elif path == "/slurm/v0.0.37/jobs":
            return {"jobs": list(jobs.values())}
        else:
            raise NotImplementedError(path)

    def _delete(
        path: str,
        request_options=None,
        error_msg: Optional[str] = None,
        raise_on_error: bool = True,
    ):
        if path.startswith("/slurm/v0.0.37/job/"):
            job_id = int(path.split("/")[-1])
            job_info = jobs.get(job_id)
            if job_info is None:
                if raise_on_error:
                    raise SlurmError(error_msg)
            else:
                job_info["job_state"] = "CANCELLED"
        else:
            raise NotImplementedError(path)

    def _post(
        path: str,
        json: Optional[dict] = None,
        request_options=None,
        raise_on_error: bool = True,
        error_msg: Optional[str] = None,
    ):
        nonlocal last_job_id
        if path == "/slurm/v0.0.37/job/submit":
            last_job_id += 1
            job_info = {"job_id": last_job_id, "job_state": "PENDING", **json["job"]}
            jobs[last_job_id] = job_info

            cmd = []
            lines = json["script"].split("\n")
            shebang = lines[0]
            if "bash" in shebang:
                if sys.platform == "win32":
                    pytest.skip("bash script does not run on windows")
                suffix = ".sh"
            elif "python" in shebang:
                if sys.platform == "win32":
                    lines.pop(0)
                    cmd = [sys.executable]
                suffix = ".py"
            else:
                assert False, f"Unknown script starting with '{shebang}'"

            with NamedTemporaryFile(
                "w", delete=False, dir=str(tmpdir), suffix=suffix
            ) as script:
                script.write("\n".join(lines))
                filename = script.name
            os.chmod(filename, 0o755)
            cmd.append(filename)

            env = json["job"]["environment"]
            env = {k: str(v) for k, v in env.items()}
            env = {**os.environ, **env}
            env["SLURM_JOB_ID"] = str(job_info["job_id"])

            if json["job"]["standard_output"] == "/dev/null":
                stdout = None
            else:
                stdout = subprocess.PIPE
            if json["job"]["standard_error"] == "/dev/null":
                stderr = None
            else:
                stderr = subprocess.PIPE

            with subprocess.Popen(
                cmd, stdout=stdout, stderr=stderr, env=env, cwd=os.getcwd()
            ) as proc:
                job_info["job_state"] = "RUNNING"
                outs, errs = proc.communicate(timeout=15)
                if stdout is not None:
                    outfile = json["job"]["standard_output"].replace(
                        "%j", str(job_info["job_id"])
                    )
                    with open(outfile, "wb") as f:
                        f.write(outs)
                if stderr is not None:
                    errfile = json["job"]["standard_error"].replace(
                        "%j", str(job_info["job_id"])
                    )
                    with open(errfile, "wb") as f:
                        f.write(errs)
                if job_info["job_state"] != "CANCELLED":
                    if proc.returncode:
                        job_info["job_state"] = "FAILED"
                    else:
                        job_info["job_state"] = "COMPLETED"

            return job_info
        else:
            raise NotImplementedError(path)

    with ExitStack() as stack:
        for cls in (SlurmBaseApi, SlurmScriptApi, SlurmPythonJobApi):
            ctx = patch.object(cls, "get", MagicMock(side_effect=_get))
            stack.enter_context(ctx)
            ctx = patch.object(cls, "post", MagicMock(side_effect=_post))
            stack.enter_context(ctx)
            ctx = patch.object(cls, "delete", MagicMock(side_effect=_delete))
            stack.enter_context(ctx)
        yield
