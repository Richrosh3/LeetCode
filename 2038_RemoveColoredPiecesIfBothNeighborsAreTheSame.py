"""
[MEDIUM]

There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors
of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice
moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to
remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to
remove pieces that are colored 'A'.

Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

Example 1:
Input: colors = "AAABABB"
Output: true
Explanation:
AAABABB -> AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.

Example 2:
Input: colors = "AA"
Output: false
Explanation:
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.

Example 3:
Input: colors = "ABBBBBBBAAA"
Output: false
Explanation:
ABBBBBBBAAA -> ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBBBBBAA -> ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.

Constraints:
1 <= colors.length <= 10^5
colors consists of only the letters 'A' and 'B'
"""

class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        A_substrings = colors.split('B')
        B_substrings = colors.split('A')

        A_moves = 0
        B_moves = 0

        for sub in A_substrings:
            if len(sub) > 2:
                A_moves += len(sub) - 2

        for sub in B_substrings:
            if len(sub) > 2:
                B_moves += len(sub) - 2

        if A_moves > B_moves:
            return True
        else:
            return False

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We split the string into two lists. A_substrings is a list of "A" substrings created by splitting the string on "B"s.
    We do the same for B_substring by splitting on "A"s. 
    
    Now we iterate through the A_substring and look for substrings with a length greater than 2. If they are less than or 
    equal to 2, we can skip them. If the substrings length is greater than two, then that means Alice can make n-2 moves
    within that substring. We keep track of those moves in A_moves. 
    
    We do the same thing above for Bob and store the number of moves in B_moves. 
    
    If A_moves is greater than B_moves, then Alice wins and we return True. Otherwise, Bob wins and we return False. 
    
    Time Complexity is O(n). More specifically it is O(n) for first split, O(n) for second split, O(A) for the first for
    loop and O(B) for the second for loop. In total it is O(n) + O(n) + O(A) + O(B) --> O(2n+A+B) --> O(n).
    
    Space Complexity is O(n) as we stored the substrings in lists. 
"""