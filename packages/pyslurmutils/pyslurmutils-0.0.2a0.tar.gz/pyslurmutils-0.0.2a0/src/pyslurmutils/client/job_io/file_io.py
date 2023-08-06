"""IO to/from SLURM python jobs over file
"""

import logging
import time
from contextlib import contextmanager
from numbers import Number
from typing import Any, Optional, Tuple
import pickle
from ..errors import PendingResultError
from ..errors import CancelledResultError
from . import base_io

logger = logging.getLogger(__name__)


class Future(base_io.Future):
    def __init__(self, job_id: int, filename: str, api_object=None) -> None:
        super().__init__(job_id, api_object=api_object)
        self._filename = filename
        self._cancelled = False
        self._finished = False
        self._result = None

    def __repr__(self):
        return f"Future({self.job_id}, {self._filename})"

    def done(self) -> bool:
        return self._cancelled or self._finished

    def cancelled(self) -> bool:
        return self._cancelled

    def cancel(self) -> bool:
        self._cancelled = True
        return True

    def _fetch(self, timeout: Optional[Number] = None) -> None:
        """
        :raises:
            PendingResultError: the job is not finished
            CancelledResultError: the job IO was cancelled
        """
        if self._finished:
            return
        t0 = time.time()
        filename = self._filename.replace("%j", str(self.job_id))
        nunpicklingerrors = 0
        while True:
            if self._cancelled:
                raise CancelledResultError(f"SLURM job {self.job_id} IO was cancelled")
            try:
                with open(filename, "rb") as f:
                    self._result = pickle.load(f)
                    self._finished = True
                    return
            except FileNotFoundError:
                pass
            except pickle.UnpicklingError:
                nunpicklingerrors += 1
                if nunpicklingerrors > 2:
                    raise
            if timeout is not None and (time.time() - t0) > timeout:
                raise PendingResultError(f"SLURM job {self.job_id} has no result yet")
            time.sleep(0.5)

    def result(self, timeout: Optional[Number] = None) -> Any:
        """Waits for the result indefinitely by default.

        :raises:
            PendingResultError: the job is not finished
            CancelledResultError: the job IO was cancelled
            Exception: the exception raised by the job
        """
        self._fetch(timeout=timeout)
        if isinstance(self._result, BaseException):
            raise self._result
        return self._result

    def exception(self, timeout: Optional[Number] = None) -> Optional[BaseException]:
        """Waits for the result indefinitely by default.

        :raises:
            PendingResultError: the job is not finished
            CancelledResultError: the job IO was cancelled
        """
        self._fetch(timeout=timeout)
        if isinstance(self._result, BaseException):
            return self._result


class JobFileIoHandler(base_io.JobIoHandler):
    @contextmanager
    def start_job_io(
        self, data: Any, infile: str, outfile: str
    ) -> Tuple[str, dict, Future]:
        with open(infile, "wb") as f:
            pickle.dump(data, f)
        environment = {"_PYSLURMUTILS_INFILE": infile, "_PYSLURMUTILS_OUTFILE": outfile}
        future = Future(job_id=-1, filename=outfile, api_object=self._api_object)
        try:
            yield _PYTHON_SCRIPT, environment, future
        finally:
            self._finalize_start_job_io(future)

    def worker_count(self):
        return 0


_PYTHON_SCRIPT = """
import os,sys,pickle
print("Python version: %s" % sys.version)
print("working directory: %s" % os.getcwd())

infile = os.environ.get("_PYSLURMUTILS_INFILE")
try:
    outfile = os.environ.get("_PYSLURMUTILS_OUTFILE")
    outfile = outfile.replace("%j", os.environ["SLURM_JOB_ID"])

    try:
        print("Reading work from", infile)
        with open(infile, "rb") as f:
            func,args,kw = pickle.load(f)

        print("Executing work:", func)
        if args is None:
            args = tuple()
        if kw is None:
            kw = dict()
        result = func(*args, **kw)
    except BaseException as e:
        import traceback
        traceback.print_exc()
        result = e

    with open(outfile, "wb") as f:
        pickle.dump(result, f)
finally:
    if infile:
        os.remove(infile)
"""
