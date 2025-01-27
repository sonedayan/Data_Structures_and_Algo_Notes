# Basically a more efficient way to search than the linear algorithm
"""
Has to do with splitting the array or list down the middle,
and comparing each half if the queried number falls withing that range
"""
from typing import List


def locate_card(cards: List, query_number: int):
    """Since cards are in decreasing order of magnitude:"""
    lowest_index = 0
    highest_index = len(cards) - 1

    """Getting the middle card"""
    while lowest_index <= highest_index:
        middle_index = (lowest_index + highest_index) // 2
        middle_number = cards[middle_index]
        print(
            f"lowest_index: {lowest_index}, highest_index: {highest_index}, middle_index: {middle_index}, "
            f"middle_number: {middle_number}")

        if middle_number == query_number:
            return middle_index
        elif middle_number < query_number:
            highest_index = middle_index - 1
        elif middle_number > query_number:
            lowest_index = middle_index + 1
    return "Nothing Showed Up Nigga...Something wrong"


result = locate_card([9, 8, 7, 6, 5, 4, 3, 2, 1], 7)

print(result)
