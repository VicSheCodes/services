"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

import pytest
from collections import Counter

def contains_duplicate(nums):
    result = Counter(nums)
    # if any(v for k, v in result.items() if v > 1):
    #     return True
    return len(result) != len(nums)
    # return False


def contains_duplicates_with_set(nums):
    print(f"{nums=}, {set(nums)=}, {len(set(nums))}, {len(nums)}")
    return len(set(nums)) != len(nums)


def contains_duplicate_efficient(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


@pytest.mark.parametrize("nums, expected", [
    ([1,2,3,1], True),
    ([1,2,3,4], False),
    ([1,1,1,3,3,4,3,2,4,2], True),
    ([1], False),
    ([], False),
    ([0,0], True),
    ([-1,-1,-2,-3], True),
    ([-1,-2,-3,-4], False)
])
def test_contains_duplicate(nums, expected):
    assert contains_duplicate(nums) == expected
    assert contains_duplicates_with_set(nums) == expected
    assert contains_duplicate_efficient(nums) == expected