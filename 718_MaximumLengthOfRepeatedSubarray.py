"""
[MEDIUM]

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        def find(nums1, nums2):
            n1 = len(nums1)
            n2 = len(nums2)
            ans = 0

            for offset in range(n2):
                count = 0
                for idx in range(n1):
                    if idx + offset >= n2:
                        break
                    if nums1[idx] == nums2[idx + offset]:
                        count += 1
                        ans = max(ans, count)
                    else:
                        count = 0

            return ans

        return max(find(nums1, nums2), find(nums2, nums1))


"""
Let n = length of nums1
Let m = length of nums2

Time Complexity: O(n*m)
Space Complexity: O(1)

Explanation: 
    Basically a sliding window problem, except that you keep track of offsets from just one of the arrays and make sure, 
    that each following number is the same.
    You have to call the function twice while switching the order of parameters because the offsets are different based 
    on the parameters. You take the max of both iterations to find the max length. 
    
    Time Complexity is O(n*m). Since we call find twice, it would technically be O(2nm) but we just simplify it to O(n*m)
    Space Complexity is O(1) because we use constant space. 
"""