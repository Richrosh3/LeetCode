"""
[MEDIUM]

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        past_sums = {0: 1}
        summy = 0
        ans = 0

        for i in nums:
            summy += i
            diff = summy - k

            # we could rewrite this as ans += past_sums.get(diff, 0)
            if diff in past_sums:
                ans += past_sums[diff]

            # we could rewrite this as past_sums = past_sums.get(summy, 0)
            if summy not in past_sums:
                past_sums[summy] = 1
            else:
                past_sums[summy] += 1

        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We go through list and keep summing up the values as we go. As we do this, we take the difference of the sum and k 
    to see if we've already seen that value in the past. If we've seen the value in the past, that means the number of 
    subarrays that equal k are being considered in our current sum. Therefore, if we see that difference, we add it to
    the ans. After checking the difference, we now increment our current sum (which symbolizes are current subarray 
    nums[0:i], to our dictionary. 
    
    After going through all values in the list, we just return ans.
    
    Time complexity is O(n) because we go through all values in nums.
    Space complexity is O(n) because worst case is all sums are unique in dictionary. 
"""