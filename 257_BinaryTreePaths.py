"""
[EASY]

Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
"""


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def pathing(root, path):
            path += str(root.val)

            if not root.right and not root.left:
                ans.append(path)
                return

            path += "->"

            if root.right:
                pathing(root.right, path)
            if root.left:
                pathing(root.left, path)

        pathing(root, "")
        return ans


"""
Time Complexity: O(n)
Space Complexity: O(n/2)

Explanation: 
    Start with empty array to hold all string paths.
    
    Create a recursive function that keeps track of current node and its path. Immediately add the value of the current
    node to the path. Check if the node has children; if not, then we have reached the end of path and we can just add
    the string to the ans array and return. 
    If node has a child, then we know we can add "->" to the path. If the node has a right child, then we recursively call
    pathing function on the right child and updated path. We do the same if left node is present.
    
    We call the recursive function beginning on the root node and an empty string. Finally we return the ans array. 
    
    Time Complexity is O(n) since we go through every node in the tree. 
    
    Space Complexity is O(n/2) because in the worst case, the tree would be a full binary tree. The number of paths in 
    the array would be determined by the number of leaves in the full binary tree. The number of leaves in a full binary
    tree is (n+1)/2 which can be simplified to O(n/2).
"""