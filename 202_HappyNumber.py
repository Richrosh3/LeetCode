"""
[EASY]

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false


Constraints:
1 <= n <= 2^31 - 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        while n not in nums:
            nums.add(n)

            n_str = str(n)

            total = 0
            for i in n_str:
                total += (int(i) ** 2)

            n = total

            if n == 1:
                return True

        return False

"""
Time Complexity: ???
Space Complexity: ???

Explanation: 
    We create a set to keep track of the list of numbers we have already encountered. We enter a while loop that will only
    allow us to leave if n ever equals 1 or if we encounter a number in our set. 
    
    There is a mathematical way of finding the sum of the square of each digit in n, but I just converted n into a string, 
    then took the power of each digit and added it to a total variable. After the summation is complete, that total variable 
    becomes our new n and the while loop continues until n becomes 1 or if we encounter a duplicate in our set. 
    
    I'm actually unsure what the time and space complexities of this problem are. I'm assuming they would be approximations, 
    and no definite answer can be given. 

    If anyone has the actual answer to the time and space complexities, please feel free to let me know your explanation!
"""