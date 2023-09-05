"""
[MEDIUM]

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        ans = ListNode()
        curr = ans

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            summy = v1 + v2 + carry
            curr.val = summy % 10
            carry = summy // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or carry:
                curr.next = ListNode()
                curr = curr.next

        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    Here are the cases.
    1) both numbers are same length of digits
    2) one of the numbers has more digits than the other
    
    *Note:  When adding numbers, you may find yourself with a carry. We have to take this into account. If we finish going
            through both linked lists and still have a carry of 1, we need to create one final ListNode with a value of 1
            
    We create a variable to track the carry, initialize ans as a ListNode (which will also be the head of our linked list), 
    and we create a variable curr to keep track of the node we are currently on. We set it equal to ans, so we are at the
    head. 
    
    We step into the while loop. We only want to keep going while l1 or l2 still have values or if carry is still 1.
    Looking at the current values of the linked lists, if they are present then we set them to variables v1 and v2.
    If l1 or l2 are None, we set v1 or v2 to 0. We then take the sum of v1, v2, and carry. 
    The current nodes value will be sum mod 10. 
    The new carry will be the floor division of sum and 10.
    We then iterate to the next nodes in l1 and l2 if they are present; setting them to None otherwise
    
    If l1 or l2 or carry are still not None, we create a new node for curr.next and iterate to that node. 
    
    At the end, we can just return ans which was the head of the linked list. 
    
    The time complexity is O(n) because the worst time complexity would be going through the whole list, plus a carry. 
    This would make it O(n+1) time which simplifies to just O(n). 
    
    The space complexity would be the same as above. If there is a carry, we create one extra node.
    Therefore, O(n+1) becomes O(n). 
"""