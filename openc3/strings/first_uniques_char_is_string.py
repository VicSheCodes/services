"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

Solution:
This solution finds the first non-repeating character in a string by using a dictionary to count the frequency
of each character. It then iterates through the string to find the first character with a count of one and returns
its index. If no such character exists, it returns -1.

Steps:
1. Create an empty dictionary to store character counts.
2. Iterate through the string and update the count for each character in the dictionary.
3. Iterate through the string again, checking the count of each character in the dictionary.
4. Return the index of the first character with a count of one.
5. If no unique character is found, return -1.
"""

s1 = "leetcode"
s2 = "loveleetcode"


def firstUniqChar(s):
    seen = {}
    for char in s:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1
    for idx, char in enumerate(s):
        if seen[char] == 1:
            return idx
    return -1

if __name__ == "__main__":
    print(f"{firstUniqChar(s1)=}")
    print(f"{firstUniqChar(s2)=}")
