"""
[EASY]

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)

        for i in range(len(nums)):
            if target - nums[i] in nums_set:
                idx = nums.index(target - nums[i])
                if i != idx:
                    return [i, idx]


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We create a set of nums so that we can use O(1) search time on the set instead of O(n) search time on the nums list. 
    We then traverse the nums list and if the difference of target and the current element is in the nums_set. If it is, 
    using the index function we find the position of that difference in the list. We have to check if the current index i 
    and idx are not the same. If they are not, we return a list of i and idx. 
    
    Time complexity is O(n) since we traverse the full nums list. 
    Space complexity is O(n) because we created nums_set which has a length of n. 
"""
