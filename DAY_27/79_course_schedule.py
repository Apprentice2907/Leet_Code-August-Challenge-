'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

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
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.'''






# Using DFS logic understandable

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            visited[course] = 1
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visited[course] = 2
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True




# Leet code best solution also DFS

# class Solution:
#     def canFinish(self, numCourses, prerequisites):
#         # Build adjacency list
#         graph = {i: [] for i in range(numCourses)}
#         for course, pre in prerequisites:
#             graph[pre].append(course)

#         visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

#         def dfs(course):
#             if visited[course] == 1:  # cycle detected
#                 return False
#             if visited[course] == 2:  # already checked, no cycle
#                 return True

#             visited[course] = 1  # mark as visiting
#             for nei in graph[course]:
#                 if not dfs(nei):
#                     return False
#             visited[course] = 2  # mark as visited
#             return True

#         for c in range(numCourses):
#             if not dfs(c):
#                 return False

#         return True