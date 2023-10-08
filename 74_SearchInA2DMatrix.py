"""
[MEDIUM]

You are given an m x n integer matrix "matrix" with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bot = mid - 1

        row = (top + bot) // 2

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False


"""
Time Complexity: O(log(m*n))
Space Complexity: O(1)

Explanation: 
    We use binary search twice since it has a time complexity of O(log(n)). 
    
    The first while loop will be the binary search to find which row the target may be on. 
    Once that loop is done, we do row = (top + bottom) // 2 to get the actual row the target is residing on. 
    The second loop, is to find the target within the row using another binary search. 
    If neither while loop returned True, then once the second while loop is complete, we can determine that the target is
    not present in the matrix. Therefore, we can immediately return False. 
    
    Time Complexity is O(log(m*n)). 
    First while loop is binary search with time O(log(m)). 
    Second while loop is binary search with time O(log(n)). 
    O(log(m) + log(n)) --> O(log(m*n)). 
    
    Space Complexity is O(1) because we did all of this in place. 
"""