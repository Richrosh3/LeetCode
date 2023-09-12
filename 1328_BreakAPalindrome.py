"""
[MEDIUM]

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase
English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b
differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically
smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.


Constraints:
1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) <= 1:
            return ""

        for letterIndex in range(len(palindrome) // 2):
            if palindrome[letterIndex] != 'a':
                return palindrome[:letterIndex] + "a" + palindrome[letterIndex + 1:]

        return palindrome[:-1] + "b"


"""
Time Complexity: O(n/2)
Space Complexity: O(1)

Explanation:
    We are basically looking for the first value of a string that is not "a", because "a" is the least lexicographic value.
    Since this is a palindrome, we only have to look at half the characters which is why we set the range of the for loop
    from 0 to half the length of palindrome. Once we find the first value that is not an "a", we return the palindrome
    with the letter at letterIndex replaced with an "a". 
    
    The only case where the above doesn't work is if the string is like "aaaaaa". In this case, we have to change the last
    character to a "b" because it is the second least lexicographic value. 
    
    The time complexity is O(n/2). Worst case is something like "aaaaaa" where we are forced to complete the for loop. 
    Space complexity is O(1) because we are only ever changing 1 character from the string. 
"""
