"""
Solution:
The trick to solving this problem efficiently is to use the two-pointer technique, leveraging the fact
that the input array is sorted.
You do not need extra space for a set or dictionary. Instead, you maintain a write pointer that tracks
the position for the next unique element. As you iterate through the array, whenever you find a new unique value,
you write it to the write pointer's position and increment the pointer. This ensures all unique elements are moved
to the front of the array in-place.

Steps:
1. If the array is empty, return 0.
2. Initialize a write pointer at index 1 (since the first element is always unique).
3. Iterate through the array from the second element onward.
4. If the current element is different from the previous one, write it to the write pointer's position and increment
the write pointer.
5. After the loop, the write pointer's value is the number of unique elements (k).
6. The first k elements of the array are the unique values in sorted order.

Tricks:
- Use the sorted property to compare only adjacent elements for uniqueness.
- Avoid extra space by writing in-place.
- The write pointer always points to the next position for a unique value.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_dup_less_efficient(nums):
    if not nums:
        return 0

    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[len(seen) - 1] = num

    print(f"Unique elements: {seen}, final array: {nums[:len(seen)]}")
    return len(seen)


def remove_dup(nums):
    if not nums:
        return 0

    write_pointer = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_pointer] = nums[i]
            write_pointer += 1

    print(f"Unique elements: {nums[:write_pointer]}")
    return write_pointer


def test_remove_dup():
    assert remove_dup([1, 1, 2]) == 2
    assert remove_dup([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert remove_dup([]) == 0
    assert remove_dup([1]) == 1
    assert remove_dup([1, 2, 3]) == 3
    assert remove_dup([1, 1, 1]) == 1
