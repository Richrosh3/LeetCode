"""
[HARD]

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NeetCodeSolution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        left_prev = ans

        while True:
            # Part 1
            kth = self.getkth(left_prev, k)
            if not kth:
                break
            nextGroup = kth.next

            # Part 2
            prev, curr = nextGroup, left_prev.next
            while curr != nextGroup:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

            # Part 3
            tmp = left_prev.next
            left_prev.next = kth
            left_prev = tmp

        return ans.next

    def getkth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    Very annoyed with this problem because I had the exact same idea as NeetCode, but I used for loops instead. For some 
    reason, this made tracking when things became None very difficult. 
    
    We can split this problem into 3 parts. 
    Part 1 is where we traverse the linked list to find where the kth element of a group is. Doing this allows us to know
    if we still have a group left or not. If we don't then we can just return our answer. If we do have a group, then we 
    can use the kth next to rearrange the pointers after reversing the group. 
    
    In Part 2, is where we do the actual reversing of a group. Here we set prev to nextGroup because we want to make the
    beginning node of a group to point to the 1st node of the next group once the reversal occurs. We also want to set
    curr to the last groups last node, which will be left_prev. 
    
    Lastly in part 3, we want to set the left_prev as the current kth node. This allows us to properly find the next kth
    node and the nextGroup. 
    
    Finally, we will break out the while loop once there are not enough nodes in a group. We return ans.next because it
    is pointing to the new head of the group. 
    
    The time complexity for this problem is O(n) since we traverse the linked list once. 
    The space complexity is O(n) because we are only creating a constant number of variables every time 
"""