from typing import Callable, List

# Function that will take another function as an argument

def function1(func: Callable[[str], str]) -> str:
    print("Function 1 is called")
    print(func("Abhishek"))
    print(func("Deep"))
    return "Success"

def main_function(name: str) -> str:
    return f"Hello, {name}!"

print(function1(main_function))
print("------------------------------------------------------------------------------------------------------")

# Function that accepts a cleaning function
def clean_data(data: List[str], cleaner: Callable[[str], str]) -> List[str]:
    return [cleaner(item) for item in data]

# A few user-defined cleaners
def strip_whitespace(text: str) -> str:
    return text.strip()

def to_lowercase(text: str) -> str:
    return text.lower()

# Real data (e.g., scraped or user-entered)
raw_data = ["  Hello  ", "  WoRLd ", "\tPython\n"]

# Use different cleaning strategies
print(clean_data(raw_data, strip_whitespace))
# ['Hello', 'WoRLd', 'Python']

print(clean_data(raw_data, to_lowercase))
# ['  hello  ', '  world ', '\tpython\n']
