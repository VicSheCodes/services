"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Solution:
The solution checks if two strings are anagrams by counting the frequency of each character in both strings using
 a dictionary. It returns True if both strings have the same character counts, regardless of order; otherwise,
 it returns False. This approach is efficient and works for any character set.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
Unicode note:
This solution works for Unicode characters as well, because Python dictionaries can use any Unicode character as a key.
No adaptation is needed for Unicode support.

Solution steps:
1. Check if the lengths of the two strings are different. If they are, return False
2. Create an empty dictionary to store character counts.
3. Iterate through the first string and update the count for each character in the dictionary.
4. Iterate through the second string, decrementing the count for each character in the dictionary.
5. If a character in the second string is not found in the dictionary or its count goes

"""

s1 = "anagram"
t1 = "nagaram"

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1
    return True
