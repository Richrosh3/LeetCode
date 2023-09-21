"""
[MEDIUM]

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

class NeetCodeSolution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            if (i < 0 or i >= rows or
                    j < 0 or j >= cols or
                    board[i][j] != "O"):
                return

            board[i][j] = "T"

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # Find regions attached to edge and change value to "T"
        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == "O" and
                        (i in [0, rows - 1] or j in [0, cols - 1])):
                    dfs(i, j)

        # Change all "O" that were not attached to border to "X"s
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Change all "T"s back to "O"s
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    From the description, we know that we have to flip "O"s that are surrounded on all 4 sides. Regions that are surrounded
    by the border of the matrix do not apply to this rule. This means all we have to do is change all the regions in the
    middle of the matrix that are not connected to any border. 
    
    NeetCode simplified this into 3 steps:
    1) Find positions on the border and run dfs to find the full region attached to the border. We then change the values
    of those positions to "T"
    2) Now we find all remaining "O"s in the middle of the matrix and change them to an "X"
    3) Lastly we change all the "T"s back to an "O"
    
    We could combine the last two steps to only do 1 traversal through the matrix, but the concept would still be the same. 
    
    Time Complexity would be O(n*m) since all three double for loops have O(n*m) time.
    O(n*m) + O(n*m) + O(n*m) --> O(3*n*m) --> O(n*m)
    
    Space Complexity is O(1) since we change the values of the matrix in place.
"""