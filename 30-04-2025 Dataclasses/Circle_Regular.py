# Class without dataclass
class Circle_Regular:
    def __init__(self, x: int = 0, y : int=0, radius: int = 1):
        self.x = x
        self.y = y
        self.radius = radius

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
    
    def __lt__ (self, other):
        print("Custem __lt__ method called")
        return (self.x, self.y, self.radius) < (other.x, other.y, other.radius)

    def asdict(self):
        return {
            'x': self.x,
            'y': self.y,
            'radius': self.radius
        }

    def astupple(self):
        return (self.x, self.y, self.radius)
