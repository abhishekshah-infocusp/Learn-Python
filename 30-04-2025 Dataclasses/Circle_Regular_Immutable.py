# Class without dataclass
class Circle_Regular_Immutable:
    def __init__(self, x: int = 0, y : int=0, radius: int = 1):
        self._x = x
        self._y = y
        self._radius = radius

    def __repr__(self):
        print("Custom __repr__ method called")
        return f"Circle(x = {self.x}, y = {self.y}, radius = {self.radius})"

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            print("Custem __eq__ method called")
            return self.x == other.x and self.y == other.y and self.radius == other.radius
        return False
    
    def __hash__(self):
        print("Custom __hash__ method called")
        return hash((self.x, self.y, self.radius))
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def radius(self):
        return self._radius
    
