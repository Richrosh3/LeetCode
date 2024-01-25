"""
[EASY]

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 10^4
"""

class Solution:
    def FizzBuzz(self, n:int) -> List[str]:
        ans = []

        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

            return ans


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    Iterate numbers between 1 and n. 
    If number is divisible by 3 and 5, add FizzBuzz to the list
    If number is only divisible by 3, add Fizz to the list
    If number is only divisible by 5, add Buzz to the list
    Otherwise, for any other number, add the number as a string to the list
    
    Time Complexity is O(n) since we go through all numbers from 1 to n.
    Space Complexity is O(n) since we add n elements to the list
"""