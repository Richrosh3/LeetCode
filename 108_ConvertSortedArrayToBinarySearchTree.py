"""
[EASY]

Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.



Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def split(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = split(left, mid - 1)
            root.right = split(mid + 1, right)

            return root

        return split(0, len(nums) - 1)


"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    We look for the number in the middle of the array and assign that as the root node, then we assign the left and right 
    children by looking for the next midpoint amongst the left and right sub-arrays and recursively calling split again.
    Once the left index becomes greater than the right index, we know that we have come down to an empty list and can
    return None. 
    By returning split(0, len(nums-1), we are returning the root node of the tree and calling the recursive function. 
    
    Time complexity is O(n) as we iterate through all elements in the list. 
    Space complexity is O(n) as we create TreeNodes for every element in the list.  
"""