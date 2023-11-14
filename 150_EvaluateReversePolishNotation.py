"""
[MEDIUM]

You are given an array of strings tokens that represent an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        symbols = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": (lambda a, b: int(a / b))
        }

        for i in tokens:
            if i in symbols and len(stack) >= 2:
                y, x = stack.pop(), stack.pop()
                z = symbols[i](x, y)
                stack.append(z)

            else:
                stack.append(int(i))

        return stack.pop()


"""
Time Complexity: O(n)
Space Complexity: O(n)
    
Explanation: 
    This problem gives the same vibe as the parentheses stack problem (LeetCode 20). We utilize a stack to keep track of 
    our integers and use lambdas to facilitate the operations. (This is a great way to learn about lambdas)
    
    We create our stack and our symbols dictionary with the symbol as the key and a lambda function as a value. We choose
    to use a dictionary because a search is O(1) and we can map the functions. 
    
    Now let's go through a for loop of the tokens list. 
    
    We can only begin using functions if the stack has 2 or more integers in it and
    if i is an operator. 
    We pop our symbols from the stack. The first one will be y, and the second will be x. This order matters for subtraction
    and division. 
    We then call the lambda symbol on x,y by mapping i to the the symbols dictionary. We then append it to the stack. 
    
    If i is an integer, we just append it to the list. 
    
    Once the for loop is complete, there will be only one value in the stack and we can return stack.pop(). 
    
    Time Complexity is O(n) as we go through every element in the for loop once. 
    Space Complexity is O(n) as the dictionary will always be constant and the stack will append n values. 
"""