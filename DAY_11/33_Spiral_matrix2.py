'''Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]'''







# logic but chatGPT coded

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]
        num = 1
        t, b, l, r = 0, n - 1, 0, n - 1

        while num <= n * n:
            for j in range(l, r + 1):
                res[t][j] = num
                num += 1
            t += 1

            for i in range(t, b + 1):
                res[i][r] = num
                num += 1
            r -= 1

            if t <= b:
                for j in range(r, l - 1, -1):
                    res[b][j] = num
                    num += 1
                b -= 1

            if l <= r:
                for i in range(b, t - 1, -1):
                    res[i][l] = num
                    num += 1
                l += 1

        return res
    








# Another logic

# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         res = [[0] * n for i in range(n)]
#         dirs = [(0,1), (1,0), (0,-1), (-1,0)]
#         d = 0
#         r, c = 0, 0
#         for num in range(1, n*n + 1):
#             res[r][c] = num
#             nr, nc = r + dirs[d][0], c + dirs[d][1]
#             if nr < 0 or nr >= n or nc < 0 or nc >= n or res[nr][nc] != 0:
#                 d = (d + 1) % 4
#                 nr, nc = r + dirs[d][0], c + dirs[d][1]
#             r, c = nr, nc
#         return res