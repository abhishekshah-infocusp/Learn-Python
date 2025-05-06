# Class with dataclass
from dataclasses import dataclass, KW_ONLY, field
from functools import total_ordering
from math import pi

@dataclass(order=True)
# @total_ordering
# @dataclass(frozen=True) # if we want to make the dataclass immutable
class Circle_Dataclass:
    # following are the instance variables
    x: int = field(repr=True, default=0, compare=False)
    y: int = field(repr=True, default=0, compare=False)
    # _: KW_ONLY
    radius: int = field(repr=False, default=1, compare=True)
    
    @property
    def area(self):
        return pi * self.radius ** 2
    
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
