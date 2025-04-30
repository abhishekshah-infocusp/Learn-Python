# Class with dataclass
from dataclasses import dataclass


@dataclass(frozen=True)
class Circle_Dataclass_Immutable:
    # following are the instance variables
    x: int = 0
    y: int = 0
    radius: int = 1