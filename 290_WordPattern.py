"""
[EASY]

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letterMap = {}
        wordMap = {}

        if len(pattern) != len(s.split()):
            return False

        for letter, word in zip(pattern, s.split()):
            if (letter in letterMap and letterMap[letter] != word) or (word in wordMap and wordMap[word] != letter):
                return False
            letterMap[letter] = word
            wordMap[word] = letter

        return True

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    This is pretty much the exact same question as LeetCode 205: Isomorphic Strings. 
    Concept requires you to create two dictionaries and make sure that each letter maps to only one word and each word only
    maps to that same letter. If a letter/word attempts to map to another word/letter then we return False. 
    If it runs through the whole for loop, then we know the pattern held true.
"""