"""
[MEDIUM]

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        while numbers:
            x = numbers.pop()

            if (x - 1) not in numbers:
                streak = 1
                while (x + 1) in numbers:
                    x += 1
                    numbers.remove(x)
                    streak += 1

                longest = max(longest, streak)
            else:
                numbers.add(x)

        return longest


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    Since sorting takes O(nlog(n)) time, we utilize a set to check if a sequential number is present since a search is 
    O(n) time. 
    
    We first create our numbers set and have our return variable largest set to 0. 
    The while loop will continue until all elements from numbers have been checked and removed. 
    We pop a number as x and we check if the value x-1 is not in numbers. 
    If it is not, then we know that x is the starting number of a sequence. We set a temp variable called streak equal 
    to 1 and enter a while loop that continually checks if the value (x+1) is present in the set. If it is, we increment 
    x, remove x from numbers, and increment the streak. When the inner while loop is complete, that means the sequence 
    has finished and we compare it to longest to see which one is larger and save the value to longest. 
    If x-1 is in the set, then we have to add x back in numbers because we do not want to disrupt any sequences.
    Once all values in numbers have been checked and removed from numbers, the while loop will exit and we will just 
    return longest
    
    Time complexity is O(n) because we check each value in numbers at most twice which would be O(2n) --> O(n). 
    Space complexity is O(n) because we created a set with the same size as nums. 
"""
