"""
[EASY]

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q) and (p.val == q.val):
            return True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Another recursive solution. 
    3 cases
        - if p and q are valid nodes AND their values are the same, return True
        - if p and q are both None, return True
        - everything else is False
        
    We only recursively call isSameTree on the child nodes in the first case, because we know there are still nodes to be
    looked at. The other two cases mean that we are at the end of the branch or we can stop looking since we know they 
    are not the same
    
    Time Complexity is O(n) since we look at every node. 
    Space Complexity is O(1) as we did not use any extra space. 
"""