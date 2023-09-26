"""
[MEDIUM]

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's
in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowMap = {i: set() for i in range(9)}
        colMap = {i: set() for i in range(9)}
        subBoxMap = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val is ".":
                    continue
                if (i // 3, j // 3) not in subBoxMap.keys():
                    subBoxMap[(i // 3, j // 3)] = set()

                if val in rowMap[i] or val in colMap[j] or val in subBoxMap[(i // 3, j // 3)]:
                    return False
                else:
                    rowMap[i].add(val)
                    colMap[j].add(val)
                    subBoxMap[(i // 3, j // 3)].add(val)

        return True

"""
Time Complexity: O(81)
Space Complexity: O(81^3)

Explanation: 
    This is actually a pretty straightforward problem when you think about it logically. We have to have ways of keeping
    track of what the numbers in the current row, current column, and current grid. Keeping track of current row and column
    are easy since we can just assign sets based on the row or col index. The key thing here is keeping track of each 3x3
    grid within the board. To do this we will use the i and j position to determine which grid the number belongs in. If 
    we do floor division on (i//3, j//3) we can get the grid position. 
    
    Now that we know how to set up our tracking data structures, we iterate through the matrix and check to see if the 
    value is already present in each map. If it is, we return False. Otherwise we go through the full matrix and return 
    True. 
    
    Time complexity is O(81) since we know the sudoku board is restricted to be a 9x9 matrix. We iterate through each position
    so the total time complexity is O(9*9) --> O(81)
    
    Space complexity is O(81^3). We will have 9 keys in each of our 3 dictionaries. Each key has a corresponding set of size
    9. Therefore 9*9*3 is O(81^3). 
"""