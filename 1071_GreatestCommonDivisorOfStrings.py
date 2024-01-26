"""
[EASY]

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one
or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfString(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(str1, str2):
            if str1 == str2:
                return str1
            elif len(str1) > len(str2):
                return gcd(str1[len(str2):], str2)
            else:
                return gcd(str1, str2[len(str1):])

        return gcd(str1, str2)


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    If we compare str1 + str2 != str2 + str1, then we know the strings will have no gcd and we can immediately return ""
    
    We then create our recursive gcd algorithm to do comparisons. 
    If str1 == str2, then we know we found the gcd and we can just return str1.
    If len(str1) > len(str2), then the gcd will have to be within str2. We remove the length of str2 from the str1 and
    call the gcd function again on the shortened str1 and str2. 
    If len(str1) < len(str2), we do the opposite of the above step. 
    
    Now we can just return a call to our recursive gcd function with the original strings as parameters
    
    Time Complexity is O(n) because in the worst case let's say str1 was "aaa...aaa" and str2 was just "a". Then str1 
    would be shortened down n times until both str1 and str2 were just "a".
    
    Space Complexity is O(n) because strings are immutable in python. So everytime we shorten one of the strings, a new
    string is being created and assigned to str1/str2.
"""
