"""
[EASY]

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterCount = {}

        for letter in magazine:
            if letter not in letterCount:
                letterCount[letter] = 1
            else:
                letterCount[letter] += 1

        for letter in ransomNote:
            if letter not in letterCount or letterCount[letter] == 0:
                return False
            else:
                letterCount[letter] -= 1

        return True

"""
Let n = size of ransomNote and let m = size of magazine
Time Complexity: O(n+m)
Space Complexity: O(m)

Explanation: 
    Creating a dictionary of all letters in the magazine and their count will help us tremendously. 
    In the first for loop, we go through all the letters in magazine. If they are not already in the dictionary, we set
    its count to 1, otherwise we increment its count by 1. This for loop will be O(m).
    The second for loop goes through all the letters in ransomNote. If the letter is not in the dictionary or if the letter
    has hit a count of 0, then we know we can return False, otherwise we decrement the count of the letter. This for loop 
    will be O(n). 
    If the for loop finishes without returning False, then we know all the letters in ransomNote are in the dictionary and
    are used. 
    
    The time complexity will therefore be O(n) + O(m) --> O(n+m) which is still linear. 
    The space complexity is just every unique letter from magazine that was put into the dictionary. In the worst case,
    the size would be O(m).
"""
