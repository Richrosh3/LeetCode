"""
[MEDIUM]

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected, and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        i_2, i_1 = 0, 0

        for i in nums:
            temp = max(i + i_2, i_1)
            i_2 = i_1
            i_1 = temp


        return i_1


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    At any position we will always be doing two comparisons: (i-2 + i) and (i-1). Between these two comparisons, we
    always want to keep track of the maximum values between them. We store the values of i-2 as i_2 and i-1 as i_1. 
    As we iterate through the list, we find the max between our two comparisons and store the answer in temp. We then 
    shift our values of i_2 to be i_1 and i_1 will obtain the temp value. 
    Once we finish the for loop, we will return the max value in i_1. 
    
    Time complexity is O(n) since we iterate through every value in nums. 
    Space complexity is O(1) as all calculations were stored in just two constant variables.
"""