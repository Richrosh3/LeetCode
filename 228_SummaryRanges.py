"""
[EASY]

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums
is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Constraints:
0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l, r = 0, 1
        ans = []

        if len(nums) == 0:
            return ans
        elif len(nums) == 1:
            ans.append(str(nums[0]))
            return ans

        ranges = [nums[l]]

        while r < len(nums):
            if nums[r] == (nums[r - 1] + 1):
                ranges.append(nums[r])
            else:
                if len(ranges) == 1:
                    ans.append(str(ranges[0]))
                else:
                    ans.append(str(ranges[0]) + "->" + str(ranges[-1]))
                l = r
                ranges = [nums[l]]
            r += 1

        if len(ranges) == 1:
            ans.append(str(ranges[0]))
        else:
            ans.append(str(ranges[0]) + "->" + str(ranges[-1]))

        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)
    
Explanation: 
    We'll use two pointers to keep track of the ranges between variables. 
    We first check for our base cases. When n=0, we return an empty list and when n = 1, we return the value in nums as a string. 
    
    After that, we can create our ranges list, which keep track of numbers in a range. We add the number at our left 
    pointer to start the list. 
    
    We then go through a while loop and have to make sure that the right pointer will never exceed the length of nums. 
    We don't have to check the left pointer because we only ever set it equal to the right pointer, so it will never go
    past r. 
    
    In the while loop, we check to see if the current pointer (r) is equal to the previous value + 1. If it is, we just add
    it to ranges list. 
    If nums[r] != nums[r-1] + 1, we know that nums[r-1] is the final value of the previous range and that nums[r] is the 
    start of a new range. If size of range is only 1, then the range is just one number, and we can append that number to 
    ans. If the size of range is greater than 1, we have to append the string version of the range to ans. We call nums[0]
    to get the first value of range, concatenate that to the -> and then concatenate that once more to the last value of 
    range by calling nums[-1]. 
    At this point we must remember to set the left pointer as the right pointer, because a new range has begun. Then we
    reset the ranges list to only have the new number. 
    
    After the while loop is complete, ranges is still not empty so we add the final values to the ans list and return ans. 

    I think in terms of time and space complexity, this is the best you can get; but, I feel my code can be cleaned up a bit
    to make it practically more efficient on memory. The ranges list may be unnecessary, since we are already keeping track
    of the start and end of ranges with l and r. If we got rid of ranges, it may be more efficient on the the actual memory 
    of a computer. 
"""