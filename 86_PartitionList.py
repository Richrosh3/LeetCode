"""
[MEDIUM]

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greaterEqual = ListNode()
        lEnd, geEnd = less, greaterEqual

        while head:
            if head.val < x:
                lEnd.next = head
                lEnd = lEnd.next
            else:
                geEnd.next = head
                geEnd = geEnd.next
            head = head.next

        lEnd.next = greaterEqual.next
        geEnd.next = None

        return less.next

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We want to create two new lists. less will contain all the nodes that are less than x. greaterEqual will contain all 
    the nodes that are greater than or equal to x. 
    We create two nodes, that are basically the "curr" nodes for their respective lists and will help us move around
    the pointers later. 
    
    We go through the given linked list. If head.val is less than x, we have lEnd become head, and then increment lEnd. 
    Otherwise, we do the same for geEnd. 
    
    In the end we just have to link the two lists together. lEnd.next will point to greaterEqual.next, which is the head 
    of the greaterEqual list. Then we have gEnd.next point to None. 
    
    Lastly, we just have to return less.next
    
    Time complexity is O(n) as we go through every node in the given linked list. 
    Space complexity is O(n) as our result is a new linked list the same size as the given linked list. 
"""
