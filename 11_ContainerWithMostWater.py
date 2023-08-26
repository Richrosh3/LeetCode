"""
[MEDIUM]

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        maxArea = 0
        i,j = 0, len(height) - 1

        while i < j:
            width = j - i
            area = min(width*height[i], width*height[j])
            maxArea = max(maxArea, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea

"""
Time Complexity: O(n)
Space Complexity: O(1)

Explanation: 
    We want the largest area, so placing i and j opposite of each will increase the width which increases the chances of 
    finding the largest area earlier on. 
    In the while loop, we first calculate the width of the area.
    We then find the minimum area because otherwise the water could overflow over the shorter line. 
    Now that we found the current area, we take the max between area and our current maxArea. 
    To find the next possible maxArea, we want to keep our largest height and change our shortest height. 
    So if the shortest wall was the left one, we move it to the right by incrementing i by 1. 
    If the shortest wall was the right one, we move it to the left by decrementing j by 1. 
"""