"""
[MEDIUM]

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is
the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        rootVal = preorder[0]
        root = TreeNode(rootVal, None, None)
        rootPos = inorder.index(rootVal)

        root.left = self.buildTree(preorder[1:rootPos+1], inorder[:rootPos])
        root.right = self.buildTree(preorder[rootPos+1:], inorder[rootPos+1:])

        return root

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    The first item in the preorder will always be the root node of that subtree. We then search for the index of that 
    value in inorder. We can then recursively call buildTree on the left and right nodes. For the left node, we want to 
    look at preOrder starting at index 1 and ending at rootPos + 1 because python is non-inclusive for arrays and inorder 
    starting at the start, and ending at the value right before rootPos. For the left node, both preorder and inorder will
    be subarrays from the next value after rootPos to the end of the array. 
    
    Here is the step by step for example 1:
        # [3,9,20,15,7]
        # [9,3,15,20,7]

        # root 
        # [|3|,9,20,15,7] 
        # [9,|3|,15,20,7]

            # root.left
            # [9]
            # [9]

            # root.right
            # [|20|,15,7]
            # [15,|20|,7]

                # root.left
                # [15]
                # [15]

                # root.right
                # [7]
                # [7]
                
    The time complexity is O(n) as we go through each node in the list. 
    The space complexity is also O(n) as we create a node for each value in the list. 
"""
