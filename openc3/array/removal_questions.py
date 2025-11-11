"""
questions involving removal concepts:

1. **Remove Duplicates**:
   - Remove duplicates from a sorted/unsorted array or linked list.
   - Remove duplicate characters from a string while maintaining order.

2. **Remove Specific Elements**:
   - Remove all occurrences of a specific value from an array in-place.
   - Remove all vowels/consonants from a string.

3. **Remove by Condition**:
   - Remove elements greater/less than a given value from an array.
   - Remove all even/odd numbers from a list.

4. **Remove Substrings**:
   - Remove all occurrences of a substring from a string.
   - Remove overlapping substrings from a string.

5. **Remove Using Index**:
   - Remove the k-th element from a list or linked list.
   - Remove elements at even/odd indices from an array.

6. **Remove in Data Structures**:
   - Remove a node from a binary tree, BST, or heap.
   - Remove a key-value pair from a dictionary or hash map.

7. **Remove Consecutive Elements**:
   - Remove consecutive duplicate elements from an array.
   - Remove consecutive repeating characters from a string.

8. **Remove with Constraints**:
   - Remove elements to make the array strictly increasing.
   - Remove the minimum number of elements to balance parentheses.

9. **Remove and Return**:
   - Remove the smallest/largest element from an array or heap.
   - Remove the middle element from a linked list.

10. **Remove in Streams**:
    - Remove duplicates from a stream of data.
    - Remove elements from a sliding window in real-time.

These questions test problem-solving, data structure knowledge, and algorithmic thinking.

"""
import logging

sorted_array = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 9, 10]
unsorted_array = [3, 10, 2, 3, 4, 2, 5, 1, 10, 3, 1, 2, 3, 4, 2, 5]

logger = logging.getLogger()

# **Remove Duplicates**

def remove_duplicates_by_converting_to_set(array=unsorted_array):
    print(f"\nRemoving duplicates by converting to set from unsorted array: {array}\n")
    if not array:
        print(f"The array is empty, nothing to remove.")
        return

    unique_elements = set(array)
    print(f"Unique elements found: {list(unique_elements)}\n")
    return list(unique_elements)

def remove_duplicates_unsorted_array(array = unsorted_array):
    print(f"\nRemoving duplicates from unsorted array: {array}\n")
    if not array:
        print(f"The array is empty, nothing to remove.")
        return
    seen = set()
    index = 0
    while index < len(array):
        if array[index] in seen:
            print(f"Removing duplicate element {array[index]} at index {index}")
            array.pop(index)
        else:
            seen.add(array[index])
            index += 1

    print(f"{array=} {seen=} ")


def remove_duplicated_sorted_array(array=sorted_array):
    print(f"Removing duplicates from sorted array: {array}")
    if not array:
        print(f"The array is empty, nothing to remove.")
        return
    write_index = 1

    for read_index in range(1, len(array)):
        if array[read_index] != array[read_index - 1]:
            array[write_index] = array[read_index]
            write_index += 1

    print(f"\nResult: {array[:write_index]=} {array[write_index:]=} {array=}\n")
    return


# **Remove Specific Elements**

# Remove elements greater/less than a given value from an array.

given_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
given_value = 30

def remove_elements_greater_than_value(array=given_array, value=given_value):
    print(f"\nRemoving elements greater than {value} from array: {array}\n")
    if not array:
        print(f"The array is empty), nothing to remove.")
        return
    if value not in array:
        print(f"The value {value} is not present in the array.")
        return
    result = [num for num in array if num > value]
    print(f"Elements greater than {value} removed: {result}\n")
    return result


def remove_elements_greater_than_value_in_place(array=given_array, value=given_value):
    print(f"\nRemoving elements greater than {value} from array: {array}\n")
    if not array:
        print(f"The array is empty), nothing to remove.")
        return
    if value not in array:
        print(f"The value {value} is not present in the array.")
        return
    print(f"Array length: {len(array)}")
    i = 0
    while i < len(array):
        print(f"Array length: {len(array)}, Current index: {i}, Current value: {array[i]}")
        if array[i] > value:
            print(f"Removing element {array[i]} at index {i}")
            array.pop(i)
        else:
            i += 1
            print(f"{i=}")
    print(f"The new array is: {array} \n")


# Remove all vowels/consonants from a string.
vowels = "aeiouAEIOU"
given_string = "Hello, World! This is a test string."

def remove_vowels_from_string(string=given_string, remove_it = vowels):
    if not string:
        print(f"The string is empty, nothing to remove.")
        return

    print(f"\nRemoving vowels from string: {string}\n")
    result = "".join(char for char in string if char not in remove_it)
    print(f"String after removing vowels: {result}\n")
    vowels_from_string = "".join(char for char in string if char.lower() in remove_it)
    print(f"Vowels removed from string: {vowels_from_string}\n")

    return result

def remove_sum_from_list(arr=None, num=12):
    """
    removes all items that their sum is equal to num
    """

    if not arr:
        print(f"The array is empty, nothing to remove.")
        return
    if len(arr) == 1:
        print(f"The array has only one element, nothing to remove.")
        return

    max_item = max(arr)
    if max_item < num/2:
        print(f"No pairs found since the maximum element {max_item} is less than half of {num}.")
        return arr

    seen = set()
    to_remove = set()

    for current in arr:
        complement = num - current
        if complement in seen:
            to_remove.add(complement)
            to_remove.add(current)
        seen.add(current)

    result = [x for x in arr if x not in to_remove]
    print(f"After removing elements from {arr} that their sum is equal to {num}, removed elements: {seen}, result: {result}")
    return arr


if __name__ == "__main__":
    # remove_duplicates_by_converting_to_set()
    # remove_duplicates_unsorted_array()
    # remove_duplicated_sorted_array()

    # res = remove_elements_greater_than_value()

    # print('~' * 50)
    # res = remove_vowels_from_string()

    # remove_sum_from_list()
    arr = [1, 11, 2, 10, 3, 9]
    num = 12
    remove_sum_from_list(arr, num)

