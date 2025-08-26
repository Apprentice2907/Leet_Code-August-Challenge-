'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3'''








# Using DFS logic simple and understandable

# class Solution(object):
#     def numIslands(self, grid):
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         count = 0

#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
#                 return
#             grid[r][c] = "0"
#             dfs(r - 1, c)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r, c + 1)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1":
#                     count += 1
#                     dfs(r, c)
#         return count









# Using simple for loop and conditional statement 

# class Solution(object):
#     def numIslands(self, grid):
#         if not grid:
#             return 0

#         rows = len(grid)
#         cols = len(grid[0])
#         count = 0

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1":
#                     count += 1
#                     grid[r][c] = "0"
#                     queue = [(r, c)]
#                     while queue:
#                         x, y = queue.pop(0)
#                         directions = [(1,0), (-1,0), (0,1), (0,-1)]
#                         for dx, dy in directions:
#                             nx, ny = x + dx, y + dy
#                             if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
#                                 grid[nx][ny] = "0"
#                                 queue.append((nx, ny))
#         return count
