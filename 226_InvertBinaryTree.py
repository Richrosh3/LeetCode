"""
[EASY]

Given the root of a binary tree, invert the tree, and return its root.



Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionWithHelperFunction:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root

    def helper(self, curr):
        if curr is None:
            return curr
        else:
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            self.helper(curr.left)
            self.helper(curr.right)

class SolutionWithoutHelper:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        else:
            self.invertTree(root.right)
            self.invertTree(root.left)
            root.left, root.right = root.right, root.left
            return root


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Recursive solutions. 
    Base case is if the node you're looking out is None, then you don't have to do anything and just return. 
    Otherwise, we want to swap the left and right child nodes, and then call the function again. 
    
    In the solution with the helper, we do the swaps first because we still have a pointer to the root node in the 
    invertTree function. This swaps the nodes starting at root, to the bottom

    In the solution without the helper, we do the recursive calls first before the swaps, because we still want to keep
    the pointer to our header which is why we are working from bottom to the top. 
    
    Time complexity is O(n) because we visit every node in the tree. 
    Space Complexity is O(1) as no new data structures were created.
"""