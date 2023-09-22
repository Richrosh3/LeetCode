"""
[MEDIUM]

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class NeetCodeSolution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])

            top += 1
            for j in range(top, bottom):
                res.append(matrix[j][right - 1])

            right -= 1
            if not (left < right and top < bottom):
                break

            for k in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][k])

            bottom -= 1
            for l in range(bottom - 1, top - 1, -1):
                res.append(matrix[l][left])

            left += 1

        return res


"""
Time Complexity: O(n*m)
Space Complexity: O(n*m)

Explanation: 
    I attempted the project with the same sort of idea, except I tried doing it recursively by passing in inner parts of
    the matrix until it became []. 
    
    For example, this was my thought process of the steps: 
    1 2 3
    4 5 6 --> 5 --> []
    7 8 9
    
    HOWEVER, THIS IS EXTREMELY DIFFICULT TO SPLICE MATRICES PRECISELY. If I wanted to splice the above matrix to just 5, 
    matrix[1:2][1:2] return [] which is not the intended output of [5]. 
    
    Because of this tediosity, I went with NeetCode's approach. 
    We have 4 pointers keeping track of our leftmost and rightmost column and our top/bottom row. 
    The while loop will continually run while satisfying the conditions of left < right and top < bottom. 
    Everytime, we finish a row or column, a increment/decrement needs to be done depending on the direction we are 
    spiraling from. 
    It is important that in the middle of the while loop that we do our conditional check again since we just inremented 
    top and decremented right. 
    After running through the while loop, we have successfully added all the values to res, so we just return res. 
    
    Time complexity is O(n*m) because we traverse the whole matrix. 
    Space complexity is O(n*m) since all values of the matrix were appended to res. 
"""
