# Practicing the type variables

from typing import TypeVar, Sequence
import random

Choosable = TypeVar("NAME")

def choose(items: Sequence[Choosable]) -> Choosable:
    """Choose and return a random item"""
    return random.choice(items)

def printSequence(seq: Sequence[Choosable]) -> None:
    """Print the sequence"""
    print("Type of obj:", type(seq[0]))
    for obj in seq:
        print(obj, end=" ")
    print()

sequence_string = "Abhishek Dhruvik Mit Nisarg Jignes".split()
sequence_int = [1, 2, 3, 4, 5]
sequence_float = [1.5, 2.5, 3.5, 4.5, 5.5]

print("Chossing random element from the different sequences...")
print(choose(sequence_string))
print(choose(sequence_int))
print(choose(sequence_float))

print("\n\nPrinting the sequences...")
print("String sequence:", printSequence(sequence_string))
print("Integer sequence:", printSequence(sequence_int))
print("Float sequence:", printSequence(sequence_float))

