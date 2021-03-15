from abc import ABC, abstractmethod
from functools import wraps


def entry_and_exit_logging(function):
    @wraps(function)
    def wrapper(event, context):
        # logger.info(f"'{context.function_name}' - entry.\nIncoming event: '{event}'")
        result = function(event, context)
        # logger.info(f"'{context.function_name}' - exit.\nResult: '{result}'")
        return result

    return wrapper


class HandlerBase(ABC):
    @entry_and_exit_logging
    @abstractmethod
    def handle(self, event, context):
        pass

# TODO: add transform, fit and predict subclasses?
