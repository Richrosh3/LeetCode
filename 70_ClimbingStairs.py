"""
[EASY]

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""


class NeetCodeSolution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one += two
            two = temp

        return one


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    This problem simulates a Fibonacci sequence, so we run the fibonacci algorithm n-2 times.
    We do n-2 times because our base cases are 1,1. 
    The final answer is stored in one so we just return one. 
    
    Time complexity is technically O(n-2), which simplifies to just O(n). 
    Space complexity is O(1) because no additional dynamic data structures were needed. 
"""