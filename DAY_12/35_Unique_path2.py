'''You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1'''









# My logic using for loop and condition

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = []  
        for i in range(m):
            row = []
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    row.append(0)
                elif i == 0 and j == 0:
                    row.append(1)
                else:
                    top = 0 if i == 0 else dp[i-1][j]
                    left = 0 if j == 0 else row[j-1]
                    row.append(top + left)
            dp.append(row)

        return dp[m-1][n-1]
















# Using algorithm

# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])

#         # Step 2: Start or end blocked
#         if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
#             return 0

#         # Step 3: Create DP table
#         dp = [[0] * n for i in range(m)]

#         # Step 4: Initialize start
#         dp[0][0] = 1

#         # Step 5: Fill DP table
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j] == 1:
#                     dp[i][j] = 0
#                 else:
#                     if i > 0:
#                         dp[i][j] += dp[i-1][j]
#                     if j > 0:
#                         dp[i][j] += dp[i][j-1]

#         # Step 6: Return result
#         return dp[m-1][n-1]
