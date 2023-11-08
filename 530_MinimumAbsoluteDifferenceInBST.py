"""
[EASY]

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = prev = 10**6

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            nonlocal ans, prev
            ans = min(ans, abs(node.val - prev))
            prev = node.val

            inorder(node.right)

        inorder(root)

        return ans


"""
Time Complexity: O(n)
Space Complexity: O(1)
    
Explanation:    
    We will traverse through the tree in orer. As we go through the tree, we will constantly find the minimum difference 
    between each node and its child. The child will be denoted as prev. We initialize prev as 10**6 because we want to
    always take the minimum value so 10**6 will act as a placeholder. 
    
    Time Complexity is O(n) because every node in the tree is traversed. 
    Space Complexity is O(1) as constant space was used. 
"""