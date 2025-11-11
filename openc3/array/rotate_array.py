"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
import logging

import pytest


def rotate_array_in_place(arr, k):
    for i in range(k):
        removed_item = arr.pop()
        arr.insert(0, removed_item)
    print(f"{arr=}")

@pytest.mark.parametrize("arr, k, expected",[
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ([1,2], 3, [2,1]),
])
def test_rotate_array_in_place(arr, k, expected):

    rotate_array_in_place(arr, k)
    assert arr == expected