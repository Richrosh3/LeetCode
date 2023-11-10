"""
[MEDIUM]

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class MySolution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        def lvl_order(root, level):
            if not root:
                return
            if level >= len(ans):
                ans.append([root.val])
            else:
                ans[level].append(root.val)
            lvl_order(root.left, level + 1)
            lvl_order(root.right, level + 1)

        lvl_order(root, 0)

        return ans


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We use a recursive solution to keep track of the current node and its level. 
    If the node is null, we would just return. 
    
    If the level is >= the len(ans) then we know that we are starting on a new level, and an array at ans[level] has not
    been created yet. Therefore, we add a new array with root to the end of ans. 
    Otherwise, we would access ans[level] and append the root. 
    
    Next we just call lvl_order on the left and right children while also making sure to increment our level. 
    
    To go through the tree, we call lvl_order on the root and set its level to 0. 
    Finally, we return ans. 
    
    Time Complexity is O(n) since we visit all node. 
    Space Complexity is O(n) because ans will be filled with n nodes. 
"""


class NeetCodeSolution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        res = []

        deq = []
        deq.append(root)

        while deq:
            deqLen = len(deq)
            level = []

            for i in range(deqLen):
                node = deq.pop(0)
                if node:
                    level.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
                if level:
                    res.append(level)

        return res


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    This is the iterative use of breadth first search. BFS is good for level by level traversal. 
    We utilize a deque to keep track of the nodes that we are currently looking at and add a nodes children to. 
    
    While the deque is non-empty, we keep track of the current length of deq to see how many nodes are needed to be popped
    from the front. 
    We have a list called level, to keep track of the nodes on a level. 
    
    Use a for loop that loops for the number of nodes per level which is determined by the length of the deque. 
    For every iteration, we pop a node from the front, append its value to level, then add the left and right children to
    the deque. 
    If level is non-empty, we add it to the output list
    Lastly, we return res. 
    
    Time Complexity is O(n) as each node is visited once. 
    
    Space Complexity is O(n). O(n) for all the nodes that fill res at the end and at most O(n/2) for the deque. 
    O(n) + O(n/2) --> O(n)
"""
