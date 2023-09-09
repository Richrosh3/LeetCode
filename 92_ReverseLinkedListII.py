"""
[MEDIUM]

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Setup
        dummy = ListNode(0, head)
        left_prev, curr = dummy, head

        # Part 1
        for i in range(left - 1):
            left_prev = curr
            curr = curr.next

        # Part 2
        prev = None
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Part 3
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Let's split this problem up into three parts. 
    We first setup our problem by having a dummy node with value of 0 and next pointer pointing to head. This helps us
    with the edge case where if the head was part of the reversal, we don't have to think about what node to return. We
    could just return dummy.next
    
    In part 1, we are just traversing the linked list until we reach the left node. We want to keep track of the node 
    before left, so we call that left_prev. 
    Once you hit part 2, we iterate (right - left + 1) nodes and reverse them. We do this exactly like LeetCode problem 206, 
    Reverse Linked List. 
    At part 3, we completed traversing through all the nodes that need to be reversed. Now we just need to set the pointers 
    to correctly match the output. Our left_prev.next.next pointer will be pointing to our current node and our 
    left_prev.next pointer will need to point to the prev.
    Lastly, we can just return dummy.next. 
    
    Time Complexity is O(n) since we are traversing through the linked list once. 
    Space Complexity is O(1) because no data structures were needed to be created. 
"""