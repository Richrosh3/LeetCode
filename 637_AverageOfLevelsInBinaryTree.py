"""
[EASY]

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence, return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1
"""


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        def bfs(root):
            if not root:
                return None

            queue = []
            queue.append(root)

            while queue:
                level_len = len(queue)
                total = 0

                for _ in range(level_len):
                    node = queue.pop(0)
                    total += node.val

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                ans.append(total/level_len)

        bfs(root)

        return ans


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    To get the average of each level, we can use bfs to track the sum of each level then divide it by the number of items
    in each level. 
    
    We create our list to return called ans. 
    Create our typical dfs algorithm but we add a couple of steps. In the while loop, we declare our level_len and total
    variables. level_len tells us how many nodes are on a certain level by taking the length of the queue before any 
    children nodes are added. We iterate through the queue up to an index of level_len and continuously pop from the left
    of the list, add its value to total and then add its possible children. Once we exit the for loop, we calculate our 
    average (total / level_len) and append it to ans. The while loop will start again, re-assign the level_len value and 
    reset total back to 0. 
    Now that we declared our function, we can call it and then immediately return ans. 
    
    Time Complexity is O(n) since we visited every node. 
    Space Complexity is O(n) because we stored every node in queue at some point.  
"""
