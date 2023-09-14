"""
[MEDIUM]

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0


Constraints:
0 <= n <= 5 * 10^6
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        table = [True for i in range(n + 1)]
        table[0] = table[1] = False

        for i in range(2, n + 1):
            if table[i] is True and 2 * i < n:
                table = self.findMultiples(table, i)
            else:
                break

        return sum(table)

    def findMultiples(self, table, num):
        index = 2 * num

        while index < len(table):
            table[index] = False

            index += num

        return table

"""
Time Complexity: O(n*log(n))
Space Complexity: O(n)

Explanation: 
    We check if n is either 0 or 1. Since neither are prime, we return False
    Then we create a list that represents all the values from 0 to n and set them to all True. 
    We know that 0 and 1 are not considered prime numbers so we set them to False. 
    
    In the for loop, we start at 2 (the first prime number) and go to n+1. If the current index is set to True, we know 
    can declare that the current index is a prime. We then take a look at all its multiples and set them to False. The
    reason I also include the (2*i) < n check is because if (2*i) is greater than n, then we are needlessly looking at
    numbers that will not even matter. So that (2*i) < n is for optimization. 
    If the current index's value is set to False, we can declare that it is not a prime, and skip it. 
    
    After we finish the for loop, we can return out number of primes. Since True is equivalent to 1 and False is equivalent
    to 0 in python, we can take the total sum of the table list. This will give us the total number of primes.
    
    The time complexity is O(n*log(n)). The for loop will go through the whole list which is O(n). The while loop will 
    technically be O(ln_i(n)), but we can just use O(log(n)) as the umbrella time complexity. Since we run the while loop
    for every number, the final time complexity will be O(n*log(n)). 
    The space complexity will be O(n) since we create a list with n+1 values. Therefore it will always be linear. 
    
"""