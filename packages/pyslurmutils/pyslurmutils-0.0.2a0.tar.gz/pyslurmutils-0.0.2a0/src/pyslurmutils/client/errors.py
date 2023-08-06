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
