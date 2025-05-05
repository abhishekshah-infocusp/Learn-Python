from typing import Sized

print("Example of sized module")

class MySized(Sized):
    def __init__(self, items):
        self._items = items  # Store any collection (list, string, etc.)

    def __len__(self) -> int:
        print("Custom __len__ method called")
        return len(self._items)

    def __repr__(self):
        print("Custom __repr__ method called")
        return f"MySized({self._items})"

# A function that works only with Sized objects
def describe(obj: Sized) -> str:
    return f"Object of type {type(obj).__name__} has length {len(obj)}"

# Using the class
my_list = MySized([1, 2, 3, 4])
my_string = MySized("Hello")

print(describe(my_list))    
print(describe(my_string))
