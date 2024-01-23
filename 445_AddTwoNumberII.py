"""
[MEDIUM]

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

7->2->4->3
   5->6->4
-----------
7->8->0->7

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]


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
    def addTwoNumbers(self, l1: Optional[LisNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0

        while l1:
            num1 = (num1 * 10) + l1.val
            l1 = l1.next

        while l2:
            num2 = (num2 * 10) + l2.val

        sum_ = num1 + num2

        curr = ListNode()

        if sum_ == 0:
            return curr

        curr = curr.next
        while sum_ > 0:
            temp = ListNode(sum_ % 10)
            sum_ = sum_ // 10
            temp.next = curr
            curr = temp

        return curr

"""
Time Complexity: O(n + m)
Space Complexity: O(n) or O(m), whichever is larger

Explanation: 
    First two while loops use the advantage of the linked lists being sorted in Most significant order to retrieve their
    actual numbers.
    We then sum those numbers and initialize curr as a default ListNode. If the sum is 0, then we would just return curr.
    Otherwise, we will set curr to curr.next which is currently None. 
    We enter the while loop on the conditional that sum_ is greater than 0. In this while loop, we will basically be breaking
    down the sum_ digit by digit and storing them in a new Linked List. To get the new digit, we create a new ListNode and
    have sum_ % 10 as the parameter. Then we will get rid of the least significant digit by doing integer division with
    sum_ // 10. Now we set temp.next (new digit) to point to curr (old digit or None). Lastly, we set curr to be temp (the new digit).
    Once we break out the while loop, we can just return curr.
    
    Time Complexity is O(n+m) because we go through each linked list once within the first two while loops. The last while
    loop will have take max n+1 or m+1 time, depending on if either n or is m larger. Putting it all together the accurate 
    time complexity would be: 
    O(n) + O(m) + O(n+1) --> O(n+m+n+1) --> O(2n+m+1) --> O(n+m)
            OR
    O(n) + O(m) + O(m+1) --> O(n+m+m+1) --> O(n+2n+1) --> O(n+m)
    
    Space Complexity is O(n) or O(m). If the sum of two numbers carries over to create a new most significant digit, then
    1 extra node would be needed to fill that position. Depending on which is larger, the accurate space complexity would
    be O(n+1) or O(m+1) which would simplify to either O(n) or O(m).
"""

"""
SOLUTION 2: 
Another solution could be to use 2 stacks to insert all digits of the linked lists into them. When you pop from the stack,
you would be accessing the least significant digits of both numbers. By keeping track of a carry, you would be essentially
be doing LeetCode #2 Add Two Numbers again. This would simplify the problem, but add some extra space and time to the 
solution.
"""