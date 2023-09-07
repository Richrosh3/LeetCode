"""
[MEDIUM]

A linked list of length n is given such that each node contains an additional random pointer, which could point to any
node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should
point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list
state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two
nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of
[val, random_index] where:
    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class NeetCodeSolution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_new = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            old_new[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = old_new[curr]
            copy.next = old_new[curr.next]
            copy.random = old_new[curr.random]
            curr = curr.next

        return old_new[head]

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation:
    This is the type of problem where I would never really understand the solution because I don't understand the point
    of the question. Like why do we really need the dictionary to keep track of old and new nodes. Why can't we just keep 
    a pointer to the head of the copies and assign the values in the second while loop. I just don't really see the purpose
    of the dictionary, if we are just creating new nodes with same values and pointers. 
    
    I drew this problem out and still don't really understand the purpose. I watched NeetCode's video and the solution 
    still does not make the solution seem any more intuitive. Not a fan of this problem. 
    
    NeetCode solution for future reference: https://www.youtube.com/watch?v=5Y2EiZST97Y
    
    Time complexity is technically O(2n) since we went through the linked list twice. 
    O(n) + O(n) --> O(2n) --> O(n)
    
    Space complexity is technically O(2n) since we created n new nodes, and a dictionary with n key:value pairs. 
    O(n) + O(n) --> O(2n) --> O(n)
"""