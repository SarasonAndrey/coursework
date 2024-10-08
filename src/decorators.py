from typing import Any


def log(filename: Any = None) -> Any:
    """Функция регистрирует детали выполнения функций"""

    def decorator(my_func: Any) -> Any:

        def wrapper(*args: Any, **kwargs: Any) -> None:
            if not filename:
                print(f"{my_func.__name__} started")
                try:
                    my_func(*args, **kwargs)
                    print(f"{my_func.__name__} ok")
                    print(f"{my_func.__name__} finished")
                except Exception as e:
                    print(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                try:
                    my_func(*args, **kwargs)
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} ok")
                except Exception as e:
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


@log(filename="mylog.txt")
@log()
def my_function(x: Any, y: Any) -> Any:
    return x + y


my_function(9, 8)
