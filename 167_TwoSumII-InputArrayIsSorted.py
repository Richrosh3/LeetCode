"""
[MEDIUM]

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.



Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            if (numbers[i] + numbers[j]) == target:
                return [i + 1, j + 1]
            if (numbers[i] + numbers[j]) < target:
                i += 1
            else:
                j -= 1

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Since the array is created in non-decreasing order, we can use that to our advantage. 
    We create two pointers: i at the start of the array and j at the end of the array. 
    If the sum of numbers[i] and numbers[j] is less than the target, then we know that increasing i will increase 
    the next sum. 
    If the sum of numbers[i] and numbers[j] is greater than the target, then we know that decreasing j will decrease
    the next sum. 
    Since the description states that there will always be a solution, we keep doing this until we finally hit the condition
    where the sum of numbers[i] and numbers[j] equals the target. We then return a List with i and j; both incremented
    by 1 since numbers is a 1-indexed array. 
    
    Since i and j will always meet at the target, the worse case time complexity will be O(n). 
    The Space Complexity will always be O(1) because we will always return a List of size 2. 
"""