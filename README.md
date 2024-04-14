# structify

## Rust like struct for python

Define a new struct:

```python
from structify import struct, impl

@struct
class Point:
    x: float
    y: float
```


And add method implementation on that struct

```python
@impl
def add(
    self: Point,
) -> float:
    return self.x + self.y
```

You can now instanciate the struct and call the method as if it was defined in the class:

```python
p = Point(1, 2)

p.add()
>> 3
```


# Limitation