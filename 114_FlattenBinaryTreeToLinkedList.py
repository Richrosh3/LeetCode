"""
[MEDIUM]

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NeetCodeSolution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return None

            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None

            last = rightTail or leftTail or root

            return last

        dfs(root)

"""
Time Complexity: O(n)
Space Complexity: O(h) 

Explanation: 
    We recursively call flatten to take each left node and stick it between root node and right node. We use dfs, to get
    us to the bottom-leftmost node first and then start from there. Left and right tail indicate the sub lists that are
    created at each step. If the left tail is present, we do the pointer swaps. Last is whatever is present at the root
    node. If there is so no rightTail, then last will be leftTail. If there is no right or left tail, then the root itself 
    is returned. 
    
    NeetCode Solution Video: https://www.youtube.com/watch?v=rKnD7rLT0lI
    
    Time complexity is O(n) since we went through every node in the list. 
    
    Space complexity would be the longest leftTail possible. On average it would be O(h) where h is height of tree. For 
    worst case, where number of nodes in tree is n and all nodes are left children. This would make worst case space 
    complexity to be O(n). 
"""