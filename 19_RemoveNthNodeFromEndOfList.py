"""
[MEDIUM]

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        slow = fast = ans

        for i in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return ans.next

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    This is another two pointer problem for a linked list. We want to traverse the linked list while also being able to
    keep track of what nodes are behind us to determine where the nth node is. 
    
    We create our dummy node ans, and then set slow and fast equal to ans. Now we want to create distance between slow
    and fast. If we do this, and traverse the array until fast hits None, then slow with be the nth node from the end of
    the linked list. We use a for loop with a range of n+1 because the range function is non-inclusive. This ensures us 
    that n nodes are between slow and fast. 
    
    Now that we have the distance between the two nodes, we traverse the linked list with a while loop until fast becomes
    None. 
    
    Finally, we know that the slow.next is the node that needs to be deleted. To delete this node, we just redirect
    slow.next to slow.next.next. 
    
    Time Complexity is O(n) as we go through the linked list only once. 
    Space Complexity is O(1) since no new data structures were created. 
"""