"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
arr = [4,1,2,1,2,9,4]

def single_number(nums):
    # result = [i for i in nums if nums.count(i) == 1]
    # print(f"{result=}")
    # assert result[0] == 4

    for i in nums:
        if nums.count(i) == 1:
            print(f"{i}")
            return i
    print(f"Nothing found")
    return None

def single_number_linear(nums):
    print(f"{nums - [set(nums)]}")

def single_number_xor(nums):
    result = 0
    for num in nums:
        result ^= num
    print(f"{result}")
    return result


if __name__ == "__main__":
    single_number_xor(arr)