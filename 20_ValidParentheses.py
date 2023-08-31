"""
[EASY]

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        q = []

        validMap = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for c in s:
            if c in validMap.keys():
                q.append(c)
            else:
                if not q:
                    return False
                if c != validMap[q.pop()]:
                    return False

        if q:
            return False

        return True

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    Using a queue here really helps keep track of what parentheses will be considered. We also use a dictionary to map 
    open and close parentheses.  
    
    We use a for loop to see every character in s. If the character is in validMap.keys(), which is an O(1) search, then 
    we can add it to our queue. If it is not in our validMap.keys(), then it must be a closing character. If the queue is
    empty, then we return False, because the string cannot be valid if a closing parentheses is left alone. If we look at
    latest opening parentheses and it does not map to our current closing parentheses, then we return False because the 
    string is not considered valid. 
    
    Once we finish the for loop, we need to check to see if the queue is not empty. If it is not empty, that means there 
    were open parentheses that were left, which makes the string invalid. 
    Otherwise the queue is empty and the string will be considered valid, so we return True. 
    
    We go through the for loop once, which means it is O(n). 
    The worse case for space complexity would be if the string was full of opening characters like "(((((((((". 
    This would mean our queue would be size of O(n).
"""
