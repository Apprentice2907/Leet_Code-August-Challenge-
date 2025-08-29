'''Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:  

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0'''









# My logic using looping and conditions

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = []
        for r in range(rows + 1):
            row = []
            for c in range(cols + 1):
                row.append(0)
            dp.append(row)

        max_side = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    )
                    if dp[i][j] > max_side:
                        max_side = dp[i][j]

        return max_side * max_side










# Leetcode best solution

class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        row_bits = [0] * n

        for i in range(n):
            bits = 0
            for j in range(m):
                if matrix[i][j] == '1':
                    bits |= (1 << j)
            row_bits[i] = bits

        l, h = 1, min(n, m)
        res = 0

        while l <= h:
            mid = (l + h) // 2
            f = False
            for i in range(n - mid + 1):
                mask = row_bits[i]
                for t in range(1, mid):
                    mask &= row_bits[i + t]
                    if mask == 0:
                        break
                if mask == 0:
                    continue
                m1 = mask
                for j in range(1, mid):
                    m1 &= (mask >> j)
                    if m1 == 0:
                        break
                if m1:
                    f = True
                    break
            if f:
                res = mid
                l = mid + 1
            else:
                h = mid - 1

        return res * res