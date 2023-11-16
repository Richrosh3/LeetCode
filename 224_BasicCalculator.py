"""
[HARD]

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of
the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""


class CrackingFAANGSolution:
    def calculate(self, s: str) -> int:

        curr = 0
        res = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                # getting our current number
                curr = curr*10 + int(c)
            elif c in ["+", "-"]:
                # add our current number to result
                res += sign * curr

                # change sign
                sign = 1 if c is "+" else -1

                # reset curr
                curr = 0
            elif c is "(":
                # saving our current result to the stack, and saving its sign
                stack.append(res)
                stack.append(sign)

                # resetting sign and result
                sign = 1
                res = 0
            elif c is ")":
                # get our current sum inside the parentheses
                res += sign * curr
                # the first pop is the sign, so we pop and multiply to result
                res *= stack.pop()
                # the second pop is previous sum, so we pop and add to result
                res += stack.pop()

                # reset curr
                curr = 0
            else:
                continue

        return res + (sign * curr)


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation:    
    I had to watch CrackingFAANG's explanation to understand this problem. 
    Here is the link to his video: https://www.youtube.com/watch?v=zsJ-J08Qgdk
    
    The logic of the algorithm is written in the comments above, but to understand why to do it, I would watch his video
    
    Time Complexity is O(n) because we go through each character of the string once. 
    
    Space Complexity is O(n) as the worst case would be if we had a string such as "(((((1)))))". In this case we would
    would append 2 elements (the result and sign) for every ")" that is visited. So technically the time complexity would
    be closer to O(2n) but it simplifies to O(n).
"""