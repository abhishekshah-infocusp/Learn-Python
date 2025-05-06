# We can use lenght on any object that has a __len__ method

import random
from typing import List, Tuple

class Random:
    def __len__(self):
        return 4987
    
r = Random()
print(len(r))

# methods with type hints and the return types
def add_numbers(a: int, b: int) -> int:
    ans = a + b
    return ans
print(add_numbers(1, 2))


pi: float = 3.14

def circle_area(radius: float) -> float:
    return pi * radius ** 2

circle_area(5)

print(__annotations__)

print(circle_area.__annotations__)

def headline(
    text,           # type: str
    width=80,       # type: int
    fill_char="-",  # type: str
):                  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)

print(headline("hello world"))



SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]
Deck = List[Card]


def create_deck(shuffle: bool=False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck) -> Tuple[Deck, Deck, Deck, Deck]: # type: ignore
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}

    for name, cards in hands.items():
        card_str = " ".join(f"{s}{r}" for (s, r) in cards)
        print(f"{name}: {card_str}")
# Annotion for list: List[T]
# Annotion for tupple: Tuple[T, T]

play()

# Functions without return types
def helloWorld() -> None:
    print("Hello World")

helloWorld()


print ("Version 2 of the card game....")
# game.py

import random
from typing import List, Tuple

SUITS = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck: # type: ignore
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]: # type: ignore
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def play() -> None:
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3}  ", end="")
        print()

play()

print("ANY.....")

import random
from typing import Any, Sequence

def choose(items: Sequence[Any]) -> Any:
    return random.choices(items)

names = ["Abhishek", "Dhruvik", "MIT", "Jignesh", "Nisarg"]


print("subclass.....")

print(int(True))
print(int(False))
print(issubclass(bool, int))
print(issubclass(int, bool))

print("TYPE VARIABLES.....")

from typing import TypeVar

Choosable = TypeVar("Choosable", str, int, float)

def choose(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

print(choose(names))
print(choose(names))
print(choose(names))
