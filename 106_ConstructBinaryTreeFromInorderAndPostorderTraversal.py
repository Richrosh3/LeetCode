"""
[MEDIUM]

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is
the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:
1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None

        rootVal = postorder[-1]
        root = TreeNode(rootVal, None, None)
        rootPos = inorder.index(rootVal)

        root.left = self.buildTree(inorder[:rootPos], postorder[:rootPos])
        root.right = self.buildTree(inorder[rootPos + 1:], postorder[rootPos:len(postorder) - 1])

        return root

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    Same concept as LeetCode 105, except that postorder stores the root node of the tree at the end of the list. 
    If we write out the step by step for the inorder and postorder lists, you can see which subarrays are needed to 
    be returned in the recursive steps. 

    Here is the step by step for example 1: 
        # [9,3,15,20,7]
        # [9,15,7,20,3]

        # root
        # [9,|3|,15,20,7]
        # [9,15,7,20,|3|]

            # root.left
            # [9]
            # [9]
    
            # root.right
            # [15,|20|,7]
            # [15,7,|20|]
    
                # root.left
                # [15]
                # [15]
        
                # root.right
                # [7]
                # [7]
    
    The time complexity is O(n) as we go through each node in the list. 
    The space complexity is also O(n) as we create a node for each value in the list. 
"""