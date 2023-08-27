"""
[MEDIUM]

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        size = float("inf")

        while r < len(nums):
            total += nums[r]
            while total >= target:
                size = min(size, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1

        if size == float("inf"):
            return 0
        else:
            return size

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We use two pointers to create a "window" that slides down the elements in the list. This window will keep track of the 
    elements that have a sum greater than or equal to the target. 
    We set size to infinity because we are looking to find the smallest value of the window size in the array. If we set it 
    to 0, then it would always return 0 because that would be the smallest size. 
    If the sum of these elements becomes greater than the 
    target, we can increment the left pointer until the windows sum becomes less than the target. As we repeatedly do this, 
    we keep track of the size of the smallest window, by taking the minimum between the current size and the size of the
    current window. 
    Once the right pointer reaches attempts to go past the size of the array, we know we can stop checking the list. 
    If size is still equal to infinity, that means a window with a total greater than or equal to the target was never 
    found. So we can return 0. Otherwise we can return the size we found. 
"""