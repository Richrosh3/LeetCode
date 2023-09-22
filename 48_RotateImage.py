"""
[MEDIUM]

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class NeetCodeSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right-left):
                top, bottom = left, right

                topLeft = matrix[top][left+i]

                matrix[top][left+i] = matrix[bottom-i][left]

                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right] = topLeft

            left += 1
            right -= 1

"""
Time Complexity: O(n^2)
Space Complexity: O(1)

Explanation: 
    We take advantage of the fact that the matrix is a n*n square. 
    If we look at an example matrix, you recognize that the rotations are happening in a square. If we do the rotations 
    for each position in the clockwise direction, you have to save a temporary variable to hold the values multiple times. 
    If you do the rotations in the counter-clockwise direction, we only have to save the topLeft position and we can 
    directly change the values for the other 3 positions. 
    
    We create variables for left and right and set the indexes to the left most and right most columns. Our while loop 
    will continually run until left and right meet. We use a for loop to keep track of how many rotations of each position 
    we have to do. For example, if we use the 3x3 matrix, then we would have to do 2 rotations for the outer layer: 
        1 2 3                       7 2 1                       7 4 1 
        4 5 6   --1st Rotation-->   4 5 6   --2nd Rotation-->   8 5 2
        7 8 9                       9 8 3                       9 6 3
    We set top and bottom equal to left and right since it is an nxn matrix. 
    We then save our topLeft value, and do our replacements of each position.
    The thing to notice is how we are using i in the for loop. By using i, we are able to determine which positions are 
    being rotated on the iterations of the for loop. Top left will move to the right 1 space, bottom left will move up 1, 
    bottom right will shift left 1, and top right will move down 1. 
    Lastly, we increment our left pointer and decrement our right pointer. This will let us move on to rotating the next 
    layer of a matrix.
    A couple examples:
                                1 2 3               |
        3x3 Matrix: Layer 1 =   4   6               |   Layer 2 =   5
                                7 8 9               |
                                
                                1    2   3   4      |
        4x4 Matrix: Layer 1 =   5            8      |   Layer 2 =    6  7
                                9           12      |               10 11
                                13  14  15  16      |
                                
    Once the while loop condition breaks, the matrix will be rotated by 90 degrees. 
    
    Time Complexity is O(n^2) as we visited each position in the nxn matrix once.
    Space Complexity is O(1) because we altered the values of the matrix in place. 
"""