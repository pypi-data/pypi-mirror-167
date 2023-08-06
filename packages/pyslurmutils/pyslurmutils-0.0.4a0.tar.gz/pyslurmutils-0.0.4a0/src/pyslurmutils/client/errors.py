from typing import List, Type


class SlurmError(RuntimeError):
    pass


class PendingResultError(RuntimeError):
    pass


class CancelledResultError(RuntimeError):
    pass


def raise_chained_errors(errors: List[str], exc_class: Type[Exception] = SlurmError):
    try:
        if len(errors) > 1:
            raise_chained_errors(errors[:-1], exc_class=exc_class)
    except exc_class as e:
        raise exc_class(errors[-1]) from e
    else:
        raise exc_class(errors[-1])


class RemoteSlurmError(SlurmError):
    def __init__(self, tb):
        self.tb = tb

    def __str__(self):
        return self.tb


def get_remote_slurm_error(exc: BaseException, tb: str) -> Exception:
    """The exception after deserialization consists of a `BaseException`
    without cause and a traceback. Return the exception with cause."""
    exc.__cause__ = RemoteSlurmError('\n"""\n%s"""' % tb)
    return exc


def reraise_remote_slurm_error(exc: BaseException, tb: str) -> None:
    """The exception after deserialization consists of a `BaseException`
    without cause and a traceback. Raise the exception with cause."""
    raise exc from RemoteSlurmError('\n"""\n%s"""' % tb)
