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
        if n <= 2:
            return 0

        table = [True for i in range(n)]
        table[0] = table[1] = False

        def findMultiple(num):
            idx = 2*num

            while idx < n:
                table[idx] = False
                idx += num

        for j in range(2, int(n**.5)+1):
            if table[j] is True and 2*j < n:
                findMultiple(j)

        return sum(table)


"""
Time Complexity: O(n*log(n))
Space Complexity: O(n)

Explanation: 
    We check if n is either 0 or 1. Since neither are prime, we return False
    Then we create a list that represents all the values from 0 to n and set them to all True. 
    We know that 0 and 1 are not considered prime numbers so we set them to False. 
    
    In the for loop, we start at 2 (the first prime number) and go to sqrt(n) + 1. This shortens down the numbers that
    need to be checked.
    If the current index is set to True, we know can declare that the current index is a prime. 
    We then take a look at all its multiples and set them to False. The reason I also include the (2*j) < n check is because 
    if (2*j) is greater than n, then we are needlessly looking at numbers that will not even matter. So that (2*j) < n 
    is for optimization. 
    
    Now we enter the while loop to eliminate multiples of prime numbers by setting their value in the table to False.
    
    After we finish the loops, we can return out number of primes. Since True is equivalent to 1 and False is equivalent
    to 0 in python, we can take the total sum of the table list. This will give us the total number of primes.
    
    The time complexity is O(n*log(n)). The for loop will go through the whole list which is O(n). The while loop will 
    technically be O(ln_i(n)), but we can just use O(log(n)) as the umbrella time complexity. Since we run the while loop
    for every number, the final time complexity will be O(n*log(n)). 
    
    The space complexity will be O(n) since we create a list with n+1 values. Therefore it will always be linear. .
"""