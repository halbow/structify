from dataclasses import dataclass
from functools import partial
import inspect


def _struct_get_attr(self, item):
    method = self.__structify__.get(item, None)
    if method is None:
        raise AttributeError(f"'{self.__name__}' object has no attribute '{item}'")
    return partial(method, self)


def struct(cls):
    cls.__structify__ = {}

    cls.__getattr__ = _struct_get_attr
    return dataclass(cls)


def impl(func):
    cls = func.__annotations__.get("self")
    if cls is None or not inspect.isclass(cls):
        raise TypeError("self attribute should be a struct")

    print(func.__name__)
    cls.__structify__[func.__name__] = func
    return func
