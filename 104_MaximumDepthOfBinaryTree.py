"""
[EASY]

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Classic recursive binary tree problem.
    Base case is if root is None, we return 0. 
    Otherwise, we want to return 1 and also check the child nodes. In the end, we will have multiple depths, but because
    we return the max of each child, in the end we will get the maximumDepth
    
    Time Complexity is O(n) as we visit every node in the tree. 
    Space Complexity is O(1) as no additional space was needed. 
"""