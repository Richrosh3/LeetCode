"""
[EASY]

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 10^4].
1 <= Node.val <= 50
0 <= val <= 50
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(-1, head)
        prev = ans
        curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return ans.next


"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We will be deleting all nodes with the value of val from the linked list. This seems easy, but we need to consider
    some edge cases. 
    1) What if the head node contains the value
    2) What if all nodes in the linked list have the value
    
    To address both, we start by creating our return Node ans with -1 as its value and head as its next. 
    We then set prev to ans and curr to head. By having these initial steps, if either case above is true, we will always 
    have ans.next to return. 
    
    Now we can enter the while loop on the condition that curr is not None. If the current nodes value is val, we can just
    change the previous node next to point to the current nodes next. Otherwise prev becomes curr and we increment curr
    to curr.next
    
    Once we break out the while loop, we return ans.next. In case #1, ans.next will point to the next node who's value is
    not val (which may not be head). In case #2, ans.next will point directly to None.
    
    Time Complexity is O(n) since we visited every node once. 
    Space Complexity is O(1) since the extra ans node created will be constant no matter the size of n. 
"""