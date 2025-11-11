"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
Solution: use the two-pointer approach: move non-zero elements forward, then fill the rest with zeros.
"""
nums_arr = [0,1,0,3,12]
no_zerro_arr = [1, 3, 12]

def move_zeros(nums):
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    for i in range(pos, len(nums)):
        nums[i] = 0
    return nums



if __name__ == "__main__":
    print(move_zeros(nums_arr))