"""
[EASY]

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.helper(root.left, root.right)

    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and not node2) or (not node1 and node2):
            return False
        if node1.val != node2.val:
            return False
        else:
            return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    First we check to see if the root itself is None. If so, return False. 
    
    Next we call the helper to see if nodes are both None, which return True. 
    Otherwise, we have to check if one is None and other is not, we return False. 
    If the node values are not equal we return False. 
    
    Finally we recursively call the helper on the left child of node 1 and right child of node 2. We and that to the 
    helper function on right child of node 1 and left child of node 2. This will result in True if tree is symmetrical, 
    otherwise False. 
    
    Time complexity is O(n) since we go through whole tree. 
    Space complexity is O(1) because no extra nodes were created. 
"""