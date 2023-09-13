"""
[EASY]

Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.



Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.

Example 3:
Input: nums = [1,-2,-3]
Output: 5

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = float("inf")

        nums.insert(0,0)
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
            minSum = min(minSum, nums[i])

        if minSum <= 0:
            return abs(minSum) + 1
        else:
            return 1

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
     We want to find a number such that starting at that number and then summing all the numbers in the list, makes every
     greater than or equal to 1. 
     
     We can do this by replacing the current value, with the sum of current and last value. We keep track of the smallest 
     sum in minSum. If it is negative, then we to get a number that equal 0 is taking the absolute value of minSum and 
     adding 1. If the number is greater than 0, that means all the numbers in the list were positive and we can default 
     to returning 1. 
     
     The tricky thing is that we need to insert 0 at the beginning of the list, otherwise we are not comparing the first 
     index to anything. If the first index happens to be negative, and the sum of the next index is positive, the algorithm
     will think that every number in the list was positive and return 1. Instead we need to return the absolute value of
     the negative number and add 1; hence why we insert a 0 to the beginning of the list. 
     
     Time complexity is O(n) since we go through every value in the list. 
     Space complexity is O(1) as we will always only add a 0 to the beginning of the list, so it will be constant time. 
"""