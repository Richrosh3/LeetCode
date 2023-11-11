"""
[EASY]

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if i + len(needle) > len(haystack):
                    break
                if haystack[i: i + len(needle)] == needle:
                    return i

        return -1


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Go through haystack and as soon as we see that the a letter in haystack matches the first letter in needle, we make
    a comparison to check if i + len(needle) > len(haystack). If yes, then we would break out of the for loop and immediately
    return -1 since we know any following attempt would also break. If i + len(needle) < len(haystack), then we check to 
    see if the strings match. If so, we return i and if not then the for loop will continue. 
    
    Time Complexity is O(n) as we go through every letter in haystack as the worst case. 
    Space Complexity is O(1) because we did not use extra space. 
"""