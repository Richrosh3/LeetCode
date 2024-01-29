"""
[EASY]

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        nums1_set = set(nums1)

        for val in nums2:
            if val in nums1_set:
                ans.add(val)

        return ans


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We first create an ans set to return in the end. We then create a set of nums1 to eliminate any duplicate values. 
    Now we enter a for loop and iterate through the nums2 list. If the current val is in the nums1_set, then we can add
    that number into the ans set. Once we finish the for loop, we can just return ans. 
    
    Time Complexity would be O(n) since we visit each value of nums2 once. 
    
    Space Complexity would be O(n). Specifically, it would be:
    O(# of shared values of nums1 and nums2) + O(# of unique value in nums1) --> 2 * O(n) in the worst case --> O(n)
"""