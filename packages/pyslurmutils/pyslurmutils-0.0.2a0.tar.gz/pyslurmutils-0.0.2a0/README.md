# pyslurmutils

SLURM utilities for Python.

## Demo

Get an access token on rnice (prints `SLURM_JWT=<token>`)

```bash
export SLURM_TOKEN=$(scontrol token lifespan=3600)
```

Run some example jobs

```bash
python3 scripts/example.py
```

Run the tests (CI or locally)

```bash
export SLURM_TOKEN=...
export SLURM_USER=...
python3 -m pytest .
```

## Execute a python function on SLURM

### High-level API

API mimics python's `concurrent.futures` API

```python
from pyslurmutils.futures import SlurmExecutor

with SlurmExecutor(
    url,
    user_name,
    token,
    log_directory=log_directory,  # for log files
    data_directory=data_directory,  # TCP when not provided
) as pool:

    future = pool.submit(sum, args=([1, 1],), pre_script="conda activate myenv")
    assert future.result() == 2
```

### Low-level API

```python
from pyslurmutils.client.pyscript import SlurmPythonJobApi

with SlurmPythonJobApi(
        url,
        user_name,
        token,
        log_directory=log_directory,  # for log files
        data_directory=data_directory,  # TCP when not provided
    ) as pyapi:

    future = pyapi.spawn(sum, args=([1, 1],), pre_script="conda activate myenv")
    job_id = future.job_id
    try:
        pyapi.wait_done(job_id)
        pyapi.print_stdout_stderr(job_id)
        assert pyapi.get_future(job_id).result() == 2
    finally:
        pyapi.clean_job_artifacts(job_id)
```
