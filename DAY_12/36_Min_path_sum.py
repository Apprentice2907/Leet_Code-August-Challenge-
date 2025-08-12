'''Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 '''












# My logic 

class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    if dp[i-1][j] < dp[i][j-1]:
                        dp[i][j] = dp[i-1][j] + grid[i][j]
                    else:
                        dp[i][j] = dp[i][j-1] + grid[i][j]

        return dp[m-1][n-1]













# Using algorithm

# class Solution(object):
#     def minPathSum(self, grid):
#         m = len(grid)
#         n = len(grid[0])

#         dp = [[0] * n for i in range(m)]

#         # Step 3: start
#         dp[0][0] = grid[0][0]

#         # Step 4: first row
#         for j in range(1, n):
#             dp[0][j] = dp[0][j-1] + grid[0][j]

#         # Step 5: first column
#         for i in range(1, m):
#             dp[i][0] = dp[i-1][0] + grid[i][0]

#         # Step 6: rest of grid
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

#         # Step 7: answer
#         return dp[m-1][n-1]
