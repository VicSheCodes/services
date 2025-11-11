"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:

-2^31 <= x <= 2^31 - 1

Solution:
This solution reverses the digits of the integer by converting it to a string, reversing the string, and converting
it back to an integer while preserving the sign. It then checks if the result is within the 32-bit signed integer
range. The runtime is O(n), where n is the number of digits in x.

Solution Steps:
1. Determine the sign of the input integer x (positive or negative).
2. Take the absolute value of x to simplify reversal.
3. Convert the absolute value to a string and reverse the string.
4. Convert the reversed string back to an integer and restore the original sign.
5. Check if the reversed integer is within the 32-bit signed integer range [-2^31, 2^31 - 1].
6. If it is within range, return the reversed integer; otherwise, return 0.
"""

x1 = 1563847412


def reverse(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    reversed_x = str(x_abs)[::-1]
    reversed_int = sign * int(reversed_x)
    if -2**31 <= reversed_int <= 2**31 - 1:
        return reversed_int
    else:
        return 0


def test_reverse(x=x1):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)

    x_rev = str(x_abs)[::-1]
    res = int(x_rev) * sign
    if -2**31 >= res >= 2**31 - 1:
        res = 0
    print(res)


if __name__ == '__main__':
    print(reverse(x1))
    test_reverse()
