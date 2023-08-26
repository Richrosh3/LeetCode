"""
[EASY]

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation:
    One way to do this is create a new reversed string with deleted non-alphanumeric characters and lowercase characters
    However, this would increase our Space Complexity to O(n). 
    
    With the solution coded above, we utilize two pointers and compare characters on opposite sides of the string. If we come 
    across an alphanumeric character, we skip it. Once the left and right pointers reach a letter, we compare their 
    lowercase letters. If they are not the same, we can immediately return False. If they are the same, we continue the 
    comparisons until the left and right pointer hit the same position. If they successfully ran through the array and meet, 
    we can certainly say the string is a palindrome. This solution allows us to iterate the string only once and keep our
    space complexity constant. 
"""