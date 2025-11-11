import pytest
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example :

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''


def test_merge_two_sorted_lists():
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [10, 11, 12]
    m = 5
    n = 2

    nums1[m:] = sorted(nums1[m:] + nums2)
    assert nums1 == [1, 2, 3, 4, 5, 6, 10, 11, 12]

def test_zip_two_lists():
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [10, 11, 12]
    n=1

    res1 = zip(nums1, nums2)
    print(f" \n {list(res1)=} ")
    res2 = [x for pair in zip(nums1, nums2) for x in pair]
    print(f" \n {res2=}")

    print(f"")