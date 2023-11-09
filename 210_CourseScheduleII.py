"""
[MEDIUM]

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
If it is impossible to finish all courses, return an empty array.



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct
course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""


class NeetCodeSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i: [] for i in range(numCourses)}
        ans = []

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for prereq in courseMap[course]:
                if dfs(prereq) == False:
                    return False

            cycle.remove(course)
            visited.add(course)
            ans.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return ans


"""
NeetCode Video: https://www.youtube.com/watch?v=Akt3glAwyfY

Time Complexity: O(V+E)
Space Complexity: O(V+E)
    
Explanation: 
    We start by creating an adjacency map to keep track of all courses and their prerequisites. 
    
    Create a list as our expected output, one set to keep track of nodes that have been visited, and one more set to 
    check if we are ever entering a cycle.
    
    Define our dfs algorithm. Check if a node is already present in the cycle set. If yes, then a cycle has been 
    established and we can return False. Check if node has already present in the visited set. If yes, then we can
    return True because that means we have already checked its prerequisites and do not need to do it again. 
    
    Now we can add our current course to the cycle set. 
    
    We check each prerequisite of the course and run dfs on each. If the dfs ever returns False, that means a cycle
    occurred and we can return False. 
    
    Remove the course from the cycle set because we are finished looking at its prerequisites. Add it to the visited set 
    since we no longer need to check its prerequisites. Append it to the output list. Return True to signify we have
    completed this branch of courses and its prerequisites. 
    
    Lastly, we need to run the dfs algorithm on all courses. If the dfs ever returns False, we return an empty list. 
    Once the last for loop completes, we can return our output list ans.
    
    Time Complexity is O(V+E)
    O(E) for the first for loop, O(V+E) for each use of dfs and O(V) for the last for loop. 
    O(E) + O(V+E) + O(V) --> O(E+V+E+V) --> O(2V + 2E) --> O(2(V+E)) --> O(V+E)
    
    Space Complexity is O(V+E)
    O(V+E) for the courseMap dict, O(V) for the worst case in the visited set, O(V) for worst case of cycle set, and O(V)
    for the output list ans. 
    O(V+E) + O(V) + O(V) + O(V) --> O(V+E+V+V+V) --> O(4V + E) --> O(V+E)
"""