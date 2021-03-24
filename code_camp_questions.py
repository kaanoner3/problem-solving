"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
"""
import math
from functools import reduce


def sum_numbers_to_react_k(arr, k):
    required_nums = {}
    for i in range(len(arr)):
        if arr[i] in required_nums.values():
            return True

        required_nums[i] = k - arr[i]


"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all 
the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_of_elements_except_self(arr):
    # total_multiply = reduce((lambda x, y: x * y), arr)
    # for i in range(len(arr)):
    #     result.append(total_multiply / arr[i])

    n = len(arr)
    result = [0] * n
    backward = [0] * n
    forward = [0] * n
    forward[0] = arr[0]
    backward[0] = arr[n - 1]

    for i in range(1, n):
        forward[i] = forward[i - 1] * arr[i]

    j = 1
    for i in range(n - 2, -1, -1):
        backward[j] = backward[j - 1] * arr[i]
        j += 1

    backward = list(reversed(backward))

    for i in range(n):
        if i == 0:
            result[i] = backward[i + 1]
            continue
        if i == n - 1:
            result[i] = forward[i - 1]
            continue

        result[i] = backward[i + 1] * forward[i - 1]

    return result
