"""
[EASY]

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if targetSum == root.val and (not root.left and not root.right):
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Explanation: 
        Base case is if node is None so we return False
        Then we check if the targetSum is equal to root.val AND both child nodes are None. This is to ensure the current 
        node is a leaf as stated by the problem. Return True.
        Otherwise we recursively call hasPathSum on the left node and subtract the current nodes value from targetSum. 
        We do the same for the right child. 
        
        We return with OR because at any point if we return True, we know the targetSum was found.
        
        Time complexity is O(n) because we have to traverse through every node. 
        Space complexity is O(1) because we did not use any extra space. 
    """