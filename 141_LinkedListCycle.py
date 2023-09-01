"""
[EASY]

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation:
    We use two pointers, slow and fast to keep track of the nodes we are on. We will be incrementing fast by 2, and slow 
    by 1 every loop. If there is a cycle in the linked list, then at some point, fast meet at the same node as slow. 
    Therefore, we know there is a cycle. If fast ever hits a None node, we know that the linked list is linear, and we 
    will break the while loop and return False. 
    
    The Time Complexity is O(n) since we are traversing the linked list once, unless there is a cycle. 
    The Space Complexity is O(1) because we never created a new data structure to keep track of the nodes. 
"""