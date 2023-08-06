import os
import time
import logging
import json
import weakref
from uuid import uuid4
from typing import Any, Callable, Mapping, Optional, Tuple
from .script import SlurmScriptApi
from .job_io import base_io
from .job_io import tcp_io
from .job_io import file_io
from . import config

logger = logging.getLogger(__name__)


class SlurmPythonJobApi(SlurmScriptApi):
    """SLURM API to submit, cancel and monitor python functions.
    This class contains job-related state (needed to handle response)."""

    def __init__(
        self,
        *args,
        data_directory=None,
        max_workers: Optional[int] = None,
        **kw,
    ):
        if data_directory:
            os.makedirs(data_directory, exist_ok=True)
        self.data_directory = data_directory
        if data_directory:
            self._io_handler = file_io.JobFileIoHandler(api_object=self)
        else:
            self._io_handler = tcp_io.JobTcpIoHandler(
                max_workers=max_workers, api_object=self
            )
        super().__init__(*args, **kw)

    @property
    def io_handler(self) -> base_io.JobIoHandler:
        return self._io_handler

    def cleanup(self, wait: bool = True, cancel_futures: bool = False) -> None:
        """Cleanup in-memory artifacts but not on-disk artifacts (see `clean_all_job_artifacts`)"""
        self._io_handler.shutdown(wait=wait, cancel_futures=cancel_futures)
        super().cleanup(wait=wait)

    def clean_all_job_artifacts(self) -> None:
        """Cleanup on-disk artifacts"""
        for job_id in self._io_handler.get_job_ids():
            self.clean_job_artifacts(job_id)

    def spawn(
        self,
        func: Callable,
        args: Optional[Tuple] = None,
        kwargs: Optional[Mapping] = None,
        pre_script: Optional[str] = None,
        post_script: Optional[str] = None,
        job_name: Optional[str] = None,
        **kw,
    ) -> base_io.Future:
        if not job_name:
            job_name = config.DEFAULT_JOB_NAME
        data = func, args, kwargs
        if self.data_directory:
            infile = f"{self.data_directory}/{job_name}.in.{str(uuid4())}.pkl"
            outfile = f"{self.data_directory}/{job_name}.out.%j.pkl"
            ctx = self._io_handler.start_job_io(data, infile, outfile)
            metadata = {"transfer": "file", "infile": infile, "outfile": outfile}
        else:
            ctx = self._io_handler.start_job_io(data)
            metadata = {"transfer": "tcp"}
        with ctx as (pyscript, environment, future):
            script = self._generate_script(
                pyscript, pre_script=pre_script, post_script=post_script
            )
            job_id = self.submit_script(
                script,
                environment=environment,
                metadata=metadata,
                job_name=job_name,
                **kw,
            )
            future.job_id = job_id
        return future

    def _generate_script(
        self,
        script: str,
        pre_script: Optional[str] = None,
        post_script: Optional[str] = None,
    ) -> str:
        if pre_script or post_script:
            if not pre_script:
                pre_script = ""
            if not post_script:
                post_script = ""
            return f"{pre_script}\n\npython3 <<EOF\n{script}EOF\n\n{post_script}"
        else:
            return f"#!/usr/bin/env python3\n{script}"

    def get_result(self, job_id: int) -> Any:
        return self._io_handler.get_job_result(job_id)

    def get_future(self, job_id: int, **kw) -> Optional[base_io.Future]:
        future = self._io_handler.get_future(job_id)
        if future is not None:
            return future
        metadata = self._get_metadata(job_id, **kw)
        if not metadata:
            return None
        if metadata["transfer"] == "file":
            file_io.Future(
                job_id=job_id,
                filename=metadata["outfile"],
                api_object=weakref.proxy(self),
            )

    def wait_done(self, job_id: int, *args, **kw) -> str:
        timeout = kw.get("timeout", None)
        t0 = time.time()
        status = super().wait_done(job_id, *args, **kw)
        if timeout is not None:
            timeout -= time.time() - t0
            timeout = max(timeout, 0)
        future = self._io_handler.get_future(job_id)
        if future is not None:
            future.exception(timeout=timeout)
        return status

    def clean_job_artifacts(self, job_id: int, raise_on_error=False, **kw):
        properties = self.get_job_properties(job_id, **kw)
        if properties is None:
            return None
        metadata = self._get_metadata(job_id, properties=properties, **kw)
        if not metadata:
            return
        if metadata["transfer"] == "file":
            self._cleanup_job_io_artifact(job_id, metadata["infile"])
            self._cleanup_job_io_artifact(job_id, metadata["outfile"])
        super().clean_job_artifacts(
            job_id, raise_on_error=raise_on_error, properties=properties, **kw
        )

    def _get_metadata(
        self, job_id: int, properties: Optional[dict] = None, **kw
    ) -> Optional[dict]:
        if properties is None:
            properties = self.get_job_properties(job_id, **kw)
        if properties is None:
            return None
        metadata = properties.get("comment")
        if metadata is None:
            return None
        return json.loads(metadata)
