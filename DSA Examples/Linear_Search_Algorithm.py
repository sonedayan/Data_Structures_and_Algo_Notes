# Problem 1:
"""
Write a program to find the position of a given number in a list of numbers, arranged in decreasing order.
Minimize the number of times the elements are accessed in the list
"""
from typing import List


# function definition
def locate_card(cards: List, query: int):
    # Creating variable position with value of 0
    position = 0
    # Creating a checking system, starting from index 0
    for card in cards:
        # Check if element at current position matches query
        if cards[position] == query:
            # Answer found, return and exit
            return position
        else:
            # Increment the position
            position = position + 1
        # Check if we have reached end of the list
        if position == len(cards):
            return "Not Found"


result = locate_card([9, 8, 7, 6, 5, 4, 3, 2, 1], 10)

print(result)
