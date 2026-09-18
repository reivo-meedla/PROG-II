class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self._width}, Height: {self._height}"


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = value
        self._width = value


def use_shape(shape):
    w = shape.width
    shape.height = 10
    expected = w * 10
    print(f"Expected area: {expected}")
    print(f"Actual area: {shape.area()}\n")

r = Rectangle(2, 3)
use_shape(r)

s = Square(5)
use_shape(s)