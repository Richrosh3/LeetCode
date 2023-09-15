"""
[MEDIUM]

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10^9
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        curr = head
        end = head
        length = 1

        while end.next:
            length += 1
            end = end.next

        k = k % length
        if k == 0:
            return head

        newEnd = 1

        while curr.next and newEnd != (length - k):
            newEnd += 1
            curr = curr.next

        newHead = curr.next
        end.next = head
        curr.next = None

        return newHead

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Check if head is None or if k is 0. In both cases, we would just return head
    
    We set up our variables and enter the while loop which finds our last node in the list and will tell us how long
    the list is. 
    
    If k is greater than the length of the linked list, then we would be wasting time doing the rotations. To save us time, 
    we take the modulus of k and length. This gives us the least amount of rotations to reach the answer. If k is 0, we
    just return head
    
    Now we create a variable called newEnd, that will help us keep track of which node to stop at and designate as the 
    new end of the list. 
    
    We do this by entering the while loop and incrementing newEnd and curr until newEnd == (length - k). 
    
    Now we have all the nodes ready to swap pointers. We first have to designate our newHead, which will be curr.next.
    The end of the list now has to point to head current head of the list, which is just head. 
    Lastly, we have to point curr.next, which is our new end node, to None. And then we just return newHead. 
    
    Time complexity is close to O(2n) because we go through the linked list once to find the length of the list. The worst
    case for the second while loop would be (n-1) steps. So O(n) + O(n-1) is basically O(2n). We can simplify O(2n) to O(n). 
    
    Space complexity is O(1), as we only create a constant number of variables every time the function is called. 
"""