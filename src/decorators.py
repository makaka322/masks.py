# import time
from typing import Any


def log(filename: Any) -> Any:
    """Декоратор, фиксирующий работу функции"""

    def my_decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # time_start = time()
                result = func(*args, **kwargs)
                # time_end = time()
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                        print(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                        print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator


def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
