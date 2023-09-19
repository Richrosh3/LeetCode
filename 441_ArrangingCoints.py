"""
[EASY]

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row
has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.


Constraints:
1 <= n <= 2^31 - 1
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:

        level = 0
        decrement = 1

        while n >= 0:
            n -= decrement

            if n < 0:
                break
            level += 1
            decrement += 1

        return level

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    This is kind of the brute force solution for this problem. 
    We subtract a value from n every level, and for every level the subtracted values increases by 1. 
    To do this, we use a while loop and decrement n until n < 0. At the same time, we keep track of our level every time 
    we loop. 
    Once you return, you will get the correct level. 
    
    Time Complexity is O(n) as we have to continually decrement until n < 0. 
    Space Complexity is O(1) as no new space was needed to store values. 
    
    There are two more popular solutions to this problem. They both require the Gaussian Equation of (x/2)*(x+1) = rows
    1 ) Use binary search from 1 to n to find the max value that is able to complete the Gaussian Equation. This would
        O(log(n)) time. 
    2)  Interpret the Gaussian Equation as a quadratic equation set equal to n and solve for x. 
        floor[(x^2)/2 + x/2] = n
        This would be O(1) time. 
"""