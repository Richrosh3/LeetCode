"""
[EASY]

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return (l + r + 1) // 2


"""
Time Complexity: O(log(n))
Space Complexity: O(1)

Explanation: 
    This is a typical binary search problem. If the number is found, we return mid. 
    If the number is never found, we would insert between l and r, which is the position (l+r+1)//2
    
    Time Complexity is O(log(n)) because we used the binary search algorithm. 
    Space Complexity is O(1) because we did the search in place. 
"""