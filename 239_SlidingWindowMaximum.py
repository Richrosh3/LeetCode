"""
[HARD]

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the
array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one
position.
Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        deq = []
        output = []

        while r < len(nums):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            if l > deq[0]:
                deq.pop(0)

            if (r+1) >= k:
                output.append(nums[deq[0]])
                l+=1
            r+=1
        return output

"""
Time Complexity: O(n)
Space Complexity: O(k)

Explanation: 
    This problem is particularly annoying because of the left and right pointers instead of just the values. When reading
    the code, things like nums[deq[-1]] can become so confusing when you try to go though an example. 
    
    If the current number you are on is greater than the previous numbers in the deque, you remove them. 
    You then add your current number to the deque. 
    
    Here is where tracking pointers is handy. If the window you are looking at is bigger than k, we have to pop from the 
    left of the deque. However, if you just check the len(deq) > k, then that would not properly pop from the deq because 
    the deque might not have k values in it as it tracks the most recent maximum value. However, if the l is greater than
    the index of the last max value, we know that we have to pop from our deque. 
    
    Lastly we append to our output when we are looking at a window. If r+1 < k, then we haven't been looking at a full
    window yet, so we just increment r. If we are looking at a full window, we append output and increment l. 
    
    Once r > len(nums, we know we have looked at all values and we just return output. 
    
    Time complexity is O(n) as we go through all values in the list
    Space complexity is O(n) as the worst case would be if k = 1 which means all values would be appended to output. 
"""