"""
[MEDIUM]

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        ans = ListNode(0, head)
        curr = ans

        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                duplicate = curr.next.next
                while duplicate and duplicate.next and duplicate.val == duplicate.next.val:
                    duplicate = duplicate.next
                curr.next = duplicate.next
            else:
                curr = curr.next

        return ans.next

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We look at if the next node and the next next node are both present. If they are, we also have to check if the next 
    node and the next next node have the same value. If they do, we loop through a while loop until the last duplicate, 
    we then change the pointer curr.next to the last duplicates next. We don't change curr just yet, because the duplicate
    could have pointed to another set of duplicates. We only increment curr if we know for sure that the next node and 
    the next next node are both present, and if the next node's vale is not the same as the next next node's value. 
    
    It is important that we start our curr at the dummy node we created in case the first node is a set of duplicates. 
    
    Time complexity is O(n) as we went through every node in the list. 
    Space complexity is O(1) as we did not add any extra space. 
"""