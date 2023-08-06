import inspect
from collections import namedtuple

Caller = namedtuple('Caller', ['module', 'function', 'line_number'])


def inspect_caller(offset: int = 0) -> Caller:
    stack = inspect.stack()[2 + offset]
    module = inspect.getmodule(stack.frame)
    return Caller(module=module.__name__ if module is not None else '',
                    function=stack.function, line_number=stack.lineno)

def format_elapsed_time(elapsed: float) -> str:
    return f'{elapsed:.4f}s' if elapsed >= 0.1 else f'{elapsed * 1000:.2f}ms'