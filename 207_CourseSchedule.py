"""
[MEDIUM]

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course
ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i: [] for i in range(numCourses)}
        classTaken = set()

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        def dfs(course):
            if course in classTaken:
                return False

            if courseMap[course] == []:
                return True

            classTaken.add(course)

            for prereq in courseMap[course]:
                res = dfs(prereq)

                if not res:
                    return False

            classTaken.remove(course)
            courseMap[course] = []

            return True

        for i in range(numCourses):
            res = dfs(i)

            if not res:
                return False

        return True

"""
Time Complexity: O(V+P)
Space Complexity: O(V)

Explanation: 
    We first create a courseMap for all courses and a set called classTaken to make sure we don't come across a cycle. 
    We then map all our prerequisites to our courses in courseMap. 
    
    Now we create a dfs algorithm to recursively determine if prerequisites were completed. 
    If a course is already in classTaken, we have come across a cycle so we can immediately return False. 
    If a courses prerequisite list is empty, that means all prerequisites have been taken and we can confidently say that 
    we are able to take this class so we return True. 
    After our bases checks, we add the course to our classTaken set. 
    We then go through all prerequisites within the courses list and run dfs on them. If at any point, the result of the 
    dfs is False, we return False. 
    We then remove the course from the classTaken set. 
    If everything has been settled at this point, then we can determine that all prerequisites have been taken, so we 
    set the prerequisite list mapped to the course as empty.
    If all prerequisites of a course and its own prerequisites have been completed, we can return True. 
    
    Lastly, we have to run the dfs method for all classes in range of numCourses. This is because there may be two separate
    classes that have no shared courses. 
    For example, [1,2] and [3,4] have no relation to each other so we would have to run the algorithm for both of them. 
    If at any point the res is False, we can immediately return False. Otherwise we return True to signify that all 
    numCourses can be completed. 
    
    Time complexity is O(V+P). For each vertex (node) we have to look at its prerequisites as well. 
    
    Space complexity is O(V) as the dictionary will be filled with numCourses amount of keys and the classTaken set will 
    at the worst case be O(V). Therefore, O(V) + O(V) --> O(2V) --> O(V)
"""