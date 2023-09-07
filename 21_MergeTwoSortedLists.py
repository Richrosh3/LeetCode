"""
[EASY]

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.



Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
class NeetCodeSolution:
    ans = ListNode()
    curr = ans

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return ans.next

"""
Time Complexity: O(n+m)
Space Complexity: O(1)

Explanation: 
    Concept of looking for next smallest value between list1 and list2 is easy. The hard part is understanding the next
    pointers of each node. 
    We go through the while loop if list1 and list2 are not None. In the loop, we compare their values, and if list1 is
    less than list2, we are basically just shifting the next pointer of our current node to be list1. Same with list2; if
    list2 is less than or equal to list1, then we shift our current node's next pointer to list2. We keep going til we get
    kicked out the while loop. 
    Now that we are out of the while loop, we still have to account for if list1 or list2 are not empty yet. We just
    check which one is not empty and point the next node to that list. The rest of the nodes will automatically be included. 
    We return ans.next because if list1 and list2 are both empty from the start, then ans.next will be None and if both 
    lists were not empty, then ans.next will just be the smallest valued node. 
    
    Time complexity is O(n+m) because we go through the nodes in both lists. 
    Space complexity is O(1) since we only create 1 new node ans. This will be constant every time. 
"""

class mySolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        if not list1 and not list2:
            return None

        ans = ListNode()
        curr = ans

        while list1 or list2:
            l1 = 1000 if not list1 else list1.val
            l2 = 1000 if not list2 else list2.val

            if l1 <= l2:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next

            if list1 or list2:
                curr.next = ListNode()
                curr = curr.next

        return ans

"""
Time Complexity: O(n+m)
Space Complexity: O(n+m)

Explanation: 
    Same idea as NeetCode solution in comparisons, but we are creating a new linked list to keep track of the merged lists.
    
    We first do our checks to see if either or both lists are empty. 
    We then create our new starting node ans and have curr point to it at first. 
    The while loop will keep going until both lists are empty. In the while loop we are comparing the values directly. 
    Since we want to keep comparing if one of the list's node value is None, we set it to 1000 because we are looking for 
    the minimum value in the comparison. As stated in the constraints, a node's value is between -100 and 100. So 1000 
    would not matter. 
    The value comparisons are the same as above solution, but this time we are changing the values of the current node, 
    and then shifting the list node to its next. 
    We then check to see if either list1 or list2 still have values, and shift our current node. 
    After we break out of the while loop, we know that both list1 and list2 are now completely traversed and we can return
    ans. 
    
    The time complexity is still O(n+m) since we traverse both lists. 
    The space complexity is O(n+m) because we created a new node for every value in both lists.
    
    On leetcode, my solution was a bit faster but obviously utilized more memory. So depending on the situation, you could 
    sacrifice a little memory for a bit more speed. It is not always bad to have a solution that uses more space. 
"""