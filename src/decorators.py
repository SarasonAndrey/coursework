from typing import Any


def log(filename: Any | None = None) -> None:
    """Декоратор регистрирует детали выполнения функций"""

    def wrapper(func):
        def inner(*args, **kwargs):


