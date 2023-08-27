"""
[MEDIUM]

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 10^5
"""
# NeetCode's cleaner solution. Same concept as mine below, just way faster.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            # checking to see if we have duplicate values of i
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # we increment l so that we skip over duplicates of l faster
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

# This solution works, but is so slow due to the amount of if statements I utilized
class slowSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if i == j or i == k or j == k:
                    continue
                else:
                    if (nums[i] + nums[j] + nums[k]) < 0:
                        j += 1
                    elif (nums[i] + nums[j] + nums[k]) > 0:
                        k -= 1
                    else:
                        trip = [nums[i], nums[j], nums[k]]
                        if trip not in ans:
                            ans.append(trip)
                        j += 1
                        k -= 1

        return ans

"""
Time Complexity: O(nlogn) + O(n^2) --> O(n^2)
Space Complexity: O(1)

Explanation: 
    We can simplify ths question down to a twoSum question if we sort the array and keep one variable constant as we look
    at the sums. 
    We simplify the array by sorting nums which is an O(nlogn) time complexity. In python, using .sort will sort the array
    in place which gives our space complexity of O(1). If we used the sorted() method, it would've created a new sorted array
    which would increase the space complexity to O(n)
    
    Now that we have a sorted array of numbers, we will iterate through the array while keeping one of the elements constant
    as we do our sums. In this case, i will be constant in every sum within its for loop. 
    Note that the problem states i!= j, i!=k, and j!=k. So to skip over duplicates faster, we can have an if statement check if 
    the previous element is the same as our current i. If that is true, we can just skip over to the next i in the for lopop.
    
    We now can solely look at our l and r pointers. If the sum of the elements at i, l, and r are greater than 0, we 
    decrement the right pointer. If the sum was greater than 0, we increment the left pointer. If the sum is equal to 0, 
    we append that sum to our result array. We don't have to worry about duplicate sums at this point because we checked
    earlier to see that no i's are the same.
    Now to speed up the process, we can check if the left pointer is equivalent to its last position. If it is, we can 
    increment l to skip over any duplicate elements in the left pointer. This is the same idea as us checking to see if we 
    have duplicate i's as before. 
    
    The Time Complexity for the operations in the for loop is O(n^2) because we loop through every iteration of i in the
    for loop and we loop through every combination of l and r in the while loop. 
    So the total time complexity would be O(nlogn), from the .sort method we used, plus O(n^2) from the operations within
    the for loop. This can be simplified to just O(n^2) since it is larger. 
"""