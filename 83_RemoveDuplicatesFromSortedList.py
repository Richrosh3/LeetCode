"""
[EASY]

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

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
        ans = ListNode(0, head)
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.next

                while duplicate.next and curr.val == duplicate.next.val:
                    duplicate = duplicate.next

                curr.next = duplicate.next

            curr = curr.next

        return ans.next

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation:
    We go through the linked list and if we find a node who's next position is same as the current. 
    We loop through until the duplicate is no more and set the curr pointer to duplicate.next.
    
    Time complexity is O(n) because we go through full linked list. 
    Space complexity is O(1) because no extra space was needed. 
"""