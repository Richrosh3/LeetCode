"""
[EASY]

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 == len(s)

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We create two pointers (p1 for s, p2 for t) and utilize a while loop to traverse the string. If we see that the 
    letter of s is the same as the letter of t, then we can increment the pointer of s. If they are not equivalent, 
    we will increment the pointer of t regardless. Once the while loop finishes running, if the pointer of s (p1) is the
    same as the length of s, we know that s is a subsequence of t and statement will return True. If p1 is less than the 
    length of s, then statement will return False. 
"""