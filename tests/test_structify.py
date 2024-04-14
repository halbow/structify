import pytest

from structify import struct, impl
from .incorrect_function import add_1, add_2


def test_structify():
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


@pytest.mark.parametrize("func", [add_1, add_2])
def test_structify_impl_with_no_self(func):
    with pytest.raises(TypeError, match="self attribute should be a struct"):
        impl(func)


def test_structify_raise_attribute_error():
    @struct
    class Point:
        x: float
        y: float

    p = Point(1, 2)

    with pytest.raises(AttributeError, match="'Point' object has no attribute 'missing_attribute'"):
        p.missing_attribute
