"""
[MEDIUM]

Given a string s, find the length of the longest substring without repeating characters.


Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        l, r = 0, 0
        size = 0

        while l <= r and r < len(s):
            if s[r] not in s_set:
                s_set.add(s[r])
                size = max(size, len(s_set))
            else:
                while s[r] in s_set:
                    s_set.remove(s[l])
                    l += 1
                s_set.add(s[r])
            r += 1

        return size

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation:
    Since we have to keep track of the longest substring as we traverse the s, it makes sense to keep two pointers tracking
    the window of the substring. 
    We could do "if s[r] not in s", but this operation is an O(n) search ever time we call it. To decrease the search time,
    we can keep track of the letters of the current substring in a set. The search time will now be O(1) every time we use
    the in operation. 
    So if the current letter of string s is not in the s_set, we can add it to the s_set and determine that current substring 
    is larger than maximum size we previously had. 
    If the current letter of string s is in the s_set, then we have to delete all the letters of the substring until we hit 
    the repeated character. We can use a while loop and constantly remove and increment the left pointer until the substring
    is full of unique characters. 
    Lastly, we increment thr right pointer every loop so we traverse the full string. 
    Once finished, we return out discovered size. 
"""