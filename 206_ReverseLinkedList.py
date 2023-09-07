"""
[EASY]

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head = prev

        return head

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We create a prev variable and set it equal to None for now, because eventually this None will be the end of the
    reversed linked list. 
    Set the current node to head and enter while loop until current becomes None. 
    In the while loop, the only thing we are really doing is switching the direction of the arrows within the linked list
    by changing the nodes of curr.next
    
    In the end curr will be pointing at None, so prev will be pointing at the last element of the linked list, which is
    also now the head of the reversed linked list. So we just return prev, or in my case to be clear I set head to prev
    and returned head. 
    
    Time complexity is O(n) since we are going through every node within the linked list. 
    Space complexity is O(1) because we are only changing the direction of the pointers and not creating any new data
    structures. 
"""