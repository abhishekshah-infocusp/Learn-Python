import math
import pytest


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width**2

    def perimeter(self):
        return 4 * self.width

class TestCircle:

    def setup_method(self, method):
        print(f"Setting up: {method.__name__}")

    def teardown_method(self, method):
        print(f"Tearing down: {method.__name__}")

    def test_area(self):
        circle = Circle(5)
        assert circle.area() == math.pi * 5**2

    def test_perimeter(self):
        circle = Circle(5)
        assert circle.perimeter() == 2 * math.pi * 5


class TestSquare:

    def setup_method(self, method):
        print(f"Setting up: {method.__name__}")

    def teardown_method(self, method):
        print(f"Tearing down: {method.__name__}")

    def test_area(self):
        square = Square(4)
        assert square.area() == 4**2

    def test_perimeter(self):
        square = Square(4)
        assert square.perimeter() == 4 * 4


@pytest.fixture
def my_rectangle():
    return Rectangle(4, 5)


@pytest.fixture
def my_rectangle2():
    return Rectangle(3, 6)


def test_area_rectangle(my_rectangle):
    assert my_rectangle.area() == 4 * 5


def test_perimeter_rectangle(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (4 + 5)


def test_not_equal(my_rectangle, my_rectangle2):
    assert my_rectangle.area() != my_rectangle2.area()
