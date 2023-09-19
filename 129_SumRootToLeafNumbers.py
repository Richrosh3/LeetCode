"""
[MEDIUM]

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example 1:
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(root, curr_num):
            if not root:
                return 0

            curr_num = 10 * curr_num + root.val
            if root.left or root.right:
                return helper(root.left, curr_num) + helper(root.right, curr_num)
            else:
                return curr_num

        res = helper(root, 0)

        return res

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation:
    We traverse down each branch, properly increment the value of curr_num by multiplying by 10 and adding the current 
    nodes value. 
    Base case is if node is None so we return None. 
    If there is still a child present, we call the helper recursively on the children with the new curr_num and sum them.
    If there are no child nodes we just return curr_num
    
    Lastly we call the helper on the root node and value 0, then return the result. 
    
    Time complexity is O(n) because we traversed every node in the tree. 
    Space complexity is O(1) because no new nodes were created. 
"""