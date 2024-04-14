from typing import Callable, Any

import pytest

from structify import struct, impl
from .incorrect_function import add_1, add_2


def test_structify() -> None:
    @struct
    class Point:
        x: float
        y: float

    @impl
    def add(
        self: Point,
    ) -> float:
        return self.x + self.y

    p = Point(1, 2)

    assert p.add() == 3


def test_structify_args() -> None:
    @struct
    class Point:
        x: float
        y: float

    @impl
    def a(
        self: Point, *args
    ) -> float:
        return self.x + self.y + sum(args)
    @impl
    def b(
        self: Point, *args, **kwargs
    ) -> float:
        return self.x + self.y + sum(args) + sum(kwargs.values())

    p = Point(1, 2)

    assert p.a(3, 4) == 10
    assert p.b(3, 4, x=5, y=6) == 21

@pytest.mark.parametrize("func", [add_1, add_2])
def test_structify_impl_with_no_self(func: Callable[..., Any]) -> None:
    with pytest.raises(TypeError, match="self attribute should be a struct"):
        impl(func)


def test_structify_raise_attribute_error() -> None:
    @struct
    class Point:
        x: float
        y: float

    p = Point(1, 2)

    with pytest.raises(AttributeError, match="'Point' object has no attribute 'missing_attribute'"):
        p.missing_attribute # type: ignore[attr-defined]
