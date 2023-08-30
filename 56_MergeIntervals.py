"""
[MEDIUM]

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""


class NeetCodeSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by the starting value of each interval
        intervals.sort(key=lambda i: i[0])
        # we can put the first interval in our output
        output = [intervals.pop(0)]

        for start, end in intervals:
            # get the end value of the last interval in output
            lastEnd = output[-1][1]

            # if start is less than the lastEnd, we can just change the end value of the last interval in output to be
            # the larger value between lastEnd and end
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # if start is greater than the lastEnd, then the intervals do not overlap and we just add the current interval
            # to output
            else:
                output.append([start, end])

        return output

"""
Time Complexity: O(nlogn)
Space Complexity: O(n)

Explanation: 
    I actually had such a frustrating time with this problem because I was trying to work out the inequalities of the
    start and end of the intervals. By the time I hit 4 if statements of inequalities, I knew this was not the correct way
    to go about this problem. 
    
    I watched NeetCode's solution, and one of the first things he said was to create a number line when dealing with interval
    problems. I drew it out and he was absolutely right. Instead of 4 or more inequalities, there was actually just one that
    needed to be done and I would have not realized that if I had not drawn the number line. 
    
    I wrote the actual explanation of the code as comments in the solution, which becomes pretty straightforward once you
    draw the number line. 
    
    The sorting from the first line would be O(nlogn) time complexity and the for loop would go through n-1 values so it would 
    be O(n-1) time complexity. 
    O(nlogn) + O(n-1) simplifies to just O(nlogn)
    
    The space complexity is just O(n) since the worst case would be all the intervals do not overlap. 
"""
