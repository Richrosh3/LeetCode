"""
[MEDIUM]

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.



Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its
next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with
'#' signifying the end of each level.

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':


        def bfs(root):
            if not root:
                return None

            q = []
            q.append(root)

            while q:
                curr_level = len(q)

                for i in range(curr_level):
                    curr = q.pop(0)

                    if not q or i >= (curr_level - 1):
                        curr.next = None
                    else:
                        curr.next = q[0]

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)

        bfs(root)

        return root

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We want to traverse each level and set a nodes next pointer to its neighbor in the same level. We can do this by using 
    a modified BFS traversal.
    In the while loop, we use curr_level to keep track of the number of nodes in the current level. We then use a for loop
    to traverse the q, for the number of nodes in that current level. If we did not use the for loop, we could be looking 
    at a neighbors child nodes while believing we are on the same level. 
    If the queue is empty or if we are at the last node (denoted by curr_level - 1), we set the next pointer to None. 
    Otherwise, we set it to it's next neighbor on the level which is at q[0]. 
    We then add child nodes if they are present. 
    Lastly, we run the bfs method on root and return root. 
    
    Time Complexity is O(n) since we traversed through the whole tree. 
    Space Complexity is O(n) because the queue would have added n nodes. 
"""