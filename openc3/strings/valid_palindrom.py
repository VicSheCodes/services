"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

s1 = "A man, a plan, a canal: Panama"
s2 = 1324
s3 = "race a car"
s4 = " , "
s5 = "abba"

list = [s1, s2, s3, s4, s5]


def strip_non_letters(s):
    return ''.join(c.lower() for c in str(s) if c.isalpha())


def is_palindrome(s):
    s = str(s)
    right, left = 0, len(s)-1

    while left < right:
        while left < right and not s[right].isalnum():
            right += 1
        while left < right and not s[left].isalnum():
            left -= 1
        if s[right].lower() != s[left].lower():
            return False
        right += 1
        left += 1
    return True

if __name__ == "__main__":
    for st in list:
        if is_palindrome(st):
            print(f"{st=} is palindrome")
        else:
            print(f"{st=} isn't palindrome")
