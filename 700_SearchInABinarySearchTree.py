"""
[EASY]

You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node
does not exist, return null.



Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


"""
* Let h = height of tree
Time Complexity: O(h)
Space Complexity: O(1)

Explanation: 
    We take advantage of the fact that this is a binary tree. 
    The base case is to check if the current node is not None. If it is then we return None. 
    We then check if the current node is the value we are looking for, if so then we return root. 
    If the value is less than the current nodes value, then we recursively call the function only on the left branch. 
    Otherwise we call the function recursively on the right branch. 
    
    Time Complexity is O(h) because the worst case is if the key is not present which means it will traverse all the way 
    down to the leaf of a branch. 
    
    Space Complexity is O(1) because this is done in place. 
"""