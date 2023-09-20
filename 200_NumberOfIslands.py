"""
[MEDIUM]

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(i, j):
            if (i < 0 or i >= rows or
                    j < 0 or j >= cols or
                    (i, j) in visited or
                    grid[i][j] != "1"):
                return
            visited.add((i, j))

            result = (dfs(i - 1, j) or
                      dfs(i + 1, j) or
                      dfs(i, j - 1) or
                      dfs(i, j + 1))

        count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count

"""
Time Complexity: O(n) 
Space Complexity: O(n)

Explanation: 
    We use dfs to go and find each part of the island and add it to the visited set. 
    We don't need to return anything in the dfs function, because we only care about finding all parts of the island. 
    In the for loop, we have to run through every position in the matrix. 
    If the position is a "1" and has not been visited yet, that is the only time we run the dfs algorithm and increment
    out count. 
    
    Finally we return count once all positions have been checked. 
    
    Time Complexity is O(m*n) as we traversed every position in the matrix. 
    Space Complexity is O(m*n) as the set will grow to add all possible island positions. In the worst case, the whole 
    matrix would be filled with "1"s which would make the set have a size of m*n.
"""