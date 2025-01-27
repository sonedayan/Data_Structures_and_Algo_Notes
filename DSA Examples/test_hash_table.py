from typing import List, Any


def two_sum(nums: List[int], target: int) -> list[int] | list[Any]:
    num_dictionary = {}

    for i, num in enumerate(nums):
        # print({"index": i, "value": num})
        compliment = target - num

        if compliment in num_dictionary:
            return [num_dictionary[compliment], i]

        num_dictionary[num] = i

    return []


#
# def twoSum(nums: List[int], target: int) -> List[int]:
#     n = len(nums)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []  # No solution found
#
#
# class Solution:
#     pass
#
#
# result = two_sum([2, 7, 11, 15], 9)
#
# print(result)

arr = [1, 2, 3, 4, 5]

length_arr = len(arr)

print(length_arr)
