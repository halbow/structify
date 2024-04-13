from dataclasses import dataclass
import inspect


def struct(cls):
    return dataclass(cls)


def impl(func):
    cls = func.__annotations__.get("self")
    if cls is None or not inspect.isclass(cls):
        raise TypeError("self attribute should be a struct")

    setattr(cls, func.__name__, func)
    return func
