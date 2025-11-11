"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

Solution:
This solution uses a two-pointer approach to swap characters from both ends of the array, moving towards the center.
It modifies the input array in-place and requires only O(1) extra memory. The runtime is O(n), where n is the length
of the string, because each character is visited at most once.
"""

s1 = ["h","e","l","l","o"]

def reverse_string(s):
    """
    Do not return anything, modify s in-place instead.
    """
    start = 0
    end = len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    print(f"{s=}")


def test_temp(x=s1):
    start = 0
    end = len(x) - 1

    while start < end:
        x[start], x[end] = x[end], x[start]
        start += 1
        end -= 1
    print(x)


if __name__ == '__main__':
    reverse_string(s1)
