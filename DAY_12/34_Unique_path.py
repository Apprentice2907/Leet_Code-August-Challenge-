'''There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down'''








# My logic using for loop and condition 

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
            








# Using algorithm Dynamic Programming
'''Idea:
We use a Dynamic Programming (DP) table where each cell (i, j) represents the number of ways to reach that cell from (0, 0).

Steps
Start with a 2D grid dp of size m × n filled with zeros.

Set all cells in first row to 1 (can only move right).

Set all cells in first column to 1 (can only move down).

For each other cell (i, j):

dp[i][j] = dp[i-1][j] + dp[i][j-1]
(paths from above + paths from left)

The answer will be in dp[m-1][n-1].'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Step 1: Create grid of zeros
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(0)
            dp.append(row)

        # Step 2: First row = 1
        for j in range(n):
            dp[0][j] = 1

        # Step 3: First column = 1
        for i in range(m):
            dp[i][0] = 1

        # Step 4: Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Step 5: Return bottom-right value
        return dp[m-1][n-1]







