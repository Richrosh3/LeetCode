"""
[EASY]

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        for letter in s_dict:
            if s_dict[letter] != t_dict.get(letter, 0):
                return False

        return True


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    First check if s and t are different lengths. If they are then they cannot be anagrams so we return False. 
    Then create two dictionaries for s and t to keep track of the frequency of letters in their strings. 
    Traverse the strings in the first for loop and get the frequency of all characters in both s and t. 
    Use another for loop to check if all letters in s_dict and t_dict have the same values. If not then we return False. 
    If the second for loop completes, we just return True.
    
    Time Complexity is O(n) because we use two for loops that traverse the length of s and s_dict. 
    O(n) + O(~n) --> O(2n) --> O(n)
    
    Space Complexity is O(n). More specifically it is O(2 * unique letters in s/t). In the worst case if all letters in 
    s and t are unique then both dictionaries would be O(n) space. 
    O(n) + O(n) --> O(2n) --> O(n) 
"""