"""
[EASY]

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""
class neetcodeSolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}

        for c1, c2 in zip(s,t):
            if (c1 in mapS and mapS[c1] != c2) or (c2 in mapT and mapT[c2] != c1):
                return False
            mapS[c1] = c2
            mapT[c2] = c1

        return True

class mySolution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = t[i]
            if t[i] not in tMap:
                tMap[t[i]] = s[i]

        for j in range(len(t)):
            if sMap[s[j]] != t[j] or tMap[t[j]] != s[j]:
                return False

        return True

"""
NeetCode's Solution
Time Complexity: O(n)
Space Complexity: O(2n) --> O(n)

My Solution: 
Time Complexity: O(2n) --> O(n)
Space ComplexityL O(2n) --> O(n)

Explanation: 
    NeetCode's solution and my solution have the exact same concept but, technically speaking, his code is a bit faster
    even though both solutions time complexity is linear. 
    
    The basic goal of this problem is create a dictionary and track which characters are mapped to each other. But you
    have to do this for both strings. If you run into a situation where a character is not in the map or the mapped character
    does not match, then we would return False. In that if statement, you have to check both maps, otherwise you may overlook
    a character that is being mapped to multiple letters, which is not allowed. 
    
    Since the length of s and t must be the same in order for the strings to be isometric, we can say the space complexity is
    O(n) + O(n) --> O(2n) --> O(n). The same can be done with my solutions time complexity. 
"""