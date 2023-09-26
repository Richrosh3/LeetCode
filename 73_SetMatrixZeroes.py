"""
[MEDIUM]

Given an m x n integer matrix "matrix", if an element is 0, set its entire row and column to 0's.

You must do it in place.



Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1


Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        # Function to change all non-zeros in the row to T's
        def setRow(row):
            for j in range(cols):
                if matrix[row][j] == 0:
                    continue
                matrix[row][j] = "T"

        # Function to change all non-zeros in the column to T's
        def setCol(col):
            for i in range(rows):
                if matrix[i][col] == 0:
                    continue
                matrix[i][col] = "T"

        # Find position with a 0, and change its rows and cols to T's
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    setRow(i)
                    setCol(j)

        # Change all T's to zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "T":
                    matrix[i][j] = 0

        return matrix

"""
Time Complexity: O(n*m)
Space Complexity: O(1)

Explanation: 
    We traverse through the matrix and if we come across a zero, we change all the non-zero values to T's in current row
    and column. We change it to T's first because we want know where a 0 was without changing it to a 0 yet because the
    next row or column may also need to know if that position was a 0. 
    We then traverse through the matrix a second time and change all the T's to 0's.
    Finally we return matrix. 
    
    Time complexity is O(n*m) because we traverse through the matrix twice plus a row and column every time a 0 is found. 
    This can be simplified to just O(n*m).
    
    Space complexity is O(1) because we made all changes in place. 
"""

