"""
[MEDIUM]

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
"""
class NeetCodeSolution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(i, j, letter):
            if letter == len(word):
                return True

            if (i < 0 or i >= rows or
                j < 0 or j >= cols or
                word[letter] != board[i][j] or
                (i, j) in visited):
                return False

            visited.add((i,j))

            result =    (dfs(i-1,j,letter+1) or
                        dfs(i+1,j,letter+1) or
                        dfs(i,j-1,letter+1) or
                        dfs(i,j+1,letter+1))

            visited.remove((i,j))

            return result

        for i in range(rows):
            for j in range(cols):
                path = dfs(i,j,0)
                if path:
                    return True

        return False

"""
* Let w = length of word
Time Complexity: O(n*m*4^w)
Space Complexity: O(n*m)

Explanation: 
    A matrix problem that wants us to find a group of objects, or sequences within a matrix will most likely always require 
    depth first search. 
    
    We create a set to keep track of our current visited nodes, as we do not want to look at past nodes within our current 
    run of the sequence. In example 1, we don't want to look at "A" again if we are already on "B". 
    
    We create our dfs function inside the exist function so we can treat board, word, rows, cols, and visited as global 
    variables rather than having to pass them into our dfs function. 
    First we see if the letter index is equal to the length of the word. If so, we know that word sequence has been completed. 
    so we can return True. 
    Next is the possibilities of returning False. 4 of the conditionals are bounds checks for the matrix, one of them checks
    to see if the current letter in the word sequence is not in our current box, and the last conditional is to make sure
    we haven't already seen it while exploring this branch. 
    Then we add that position in the matrix as a tuple into visited. 
    Now, we can recursively call our dfs function to search for the next letter in the word. We call it for up, down, 
    left, and right. 
    If the branch has not been completed by now, we can remove the current position from visited, as we may need to visit
    it again if another possible sequence is found. 
    Then we return the result, which indicates if the next letter has been found or if the word has been complete. 
    
    Now, we just have to brute force look through all the positions in the matrix using our dfs algorithm. If the dfs 
    returns True, then we can immediately stop as we have completed the word. Otherwise, the for loops will finish, 
    meaning the word was not found, thus we return False. 
    
    Time complexity is O(n*m*4^w). O(n*m) for the bottom for loops because we search through every position in the matrix. 
    But we also called dfs on the up, down, left, and right positions for every box in which the possible sequence was. 
    This would be O(4^w) for the depth first search. Therefore, the final time complexity would be O(n*m*4^w). 
    
    Space complexity would just be O(n*m) as we are keeping track of all the positions in the matrix. 
"""