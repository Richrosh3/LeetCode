"""
[MEDIUM]

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""

class NeetCodeSolution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    This solution can be done with DP, but I hate DP so we'll go with NeetCode's greedy solution. 
    
    We start at the last position of the list and label it as our goal. We decrement our position and see if that position
    plus the positions value is greater than or equal to our current goal. If it is, we know that we can reach that goal, 
    and we re-assign our goal as the position we are currently on. Now on the next iteration of the for loop, we do the
    same thing to check if we can ever reach our current goal. 
    At the end of our for loop, the goal should be position 0. This means we can fully jump the list, so we return True. 
    If the goal is not 0, then we did not make it fully across and return False. 
    
    Time complexity is O(n) since we decrement from the last position to the first position linearly. 
    Space complexity is O(1) because no extra storage was utilized. 
"""