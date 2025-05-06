# Class with dataclass
from dataclasses import dataclass, KW_ONLY, InitVar, Field, field
from functools import total_ordering
from math import pi

@dataclass(order=True)
# @total_ordering
# @dataclass(frozen=True) # if we want to make the dataclass immutable
class Circle_DataclassPostInit:
    # following are the instance variables
    x: int = 0
    y: int = 0
    radius: int = 1
    area: float = field(init=False, repr=True)
    _: KW_ONLY
    translate_x: InitVar[int] = 0
    translate_y: InitVar[int] = 0

    def __post_init__(self, translate_x: int, translate_y: int):
        print("Post InIT is called")
        print("translatring center by x and y")
        self.x += translate_x
        self.y += translate_y
        self.area = pi * self.radius ** 2


    # @property
    # def area(self):
    #     return pi * self.radius ** 2

    # @property
    # def area(self):
    #     return self._area

    def circumference(self):
        return 2 * pi * self.radius
    
    # def __lt__(self, other):
    #     print("Custem __lt__ method called")
    #     if self.__class__ == other.__class__:
    #         return dist((0,0), (self.x, self.y)) < dist((0,0), (other.x, other.y))
    #     return NotImplemented
    
    # def __eq__(self, other):
    #     print("Custem __eq__ method called")
    #     if self.__class__ == other.__class__:
    #         return self.x == other.x and self.y == other.y and self.radius == other.radius
    #     return NotImplemented
