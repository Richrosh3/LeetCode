"""
[EASY]

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""
class Solution:
    def containsNearbyDuplicates(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    Another sliding window problem, but this time we keep track of seen elements in a set. 
    If the window size is greater than k, we just remove an element from the window and increment L. 
    At any point, if a number is already in the window then we return True. Each loop, we add the number at the right 
    pointer to the window. If the for loop completes, then we know there were no duplicates in the list. 
    
    Time complexity is O(n) because we go through the for loop once. 
    Space complexity is O(n), technically O(k), because the size of the window will always be less than or equal to k. 
"""