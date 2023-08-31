"""
[MEDIUM]

You are given an array of non-overlapping intervals "intervals" where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            currStart, currEnd = intervals[i]

            # add newInterval if it is smaller and does not overlap with current interval.
            # then return ans and rest of the intervals
            if newInterval[1] < currStart:
                ans.append(newInterval)
                return ans + intervals[i:]

            # add current interval if it is smaller and does not overlap with newInterval
            elif newInterval[0] > currEnd:
                ans.append(intervals[i])

            # newInterval overlaps, so we merge the newInterval and currentInterval
            else:
                newInterval = [min(newInterval[0], currStart), max(newInterval[1], currEnd)]

        # We have finished going through while loop which means newInterval has finished merging and is the last
        # interval in the list
        ans.append(newInterval)

        return ans

"""
Time Complexity: O(n)
Space Complexity: O(n)

Explanation: 
    I think interval questions are some of my least favorite problems, but they have become easier once I started actually 
    drawing out the intervals on a number line and looking at the relationship. 
    Anyways, the comments within the solution is basically the explanation to the though process behind the question. 
    
    In terms of time complexity, it is O(n) since we are going through the intervals list once. 
    The space complexity is O(n) because in the worst case, all intervals would not overlap and would be put inside ans.
"""