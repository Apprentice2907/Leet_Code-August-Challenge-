'''Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''







# My logic but chatGPT coded

from numpy import matrix


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        top, bot = 0, len(matrix) - 1
        lef, rig = 0, len(matrix[0]) - 1

        while lef <= rig and top <= bot:
            for i in range(lef, rig + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bot + 1):
                res.append(matrix[i][rig])
            rig -= 1

            if top <= bot:
                for i in range(rig, lef - 1, -1):
                    res.append(matrix[bot][i])
                bot -= 1

            if lef <= rig:
                for i in range(bot, top - 1, -1):
                    res.append(matrix[i][lef])
                lef += 1

        return res
            









# spiral traversal chatGPT


# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#         res = []
#         top, bot = 0, len(matrix) - 1
#         lef, rig = 0, len(matrix[0]) - 1

#         while lef <= rig and top <= bot:
#             res.extend(matrix[top][lef:rig+1]); top += 1
#             res.extend(matrix[i][rig] for i in range(top, bot+1)); rig -= 1
#             if top <= bot:
#                 res.extend(matrix[bot][rig:lef-1:-1]); bot -= 1
#             if lef <= rig:
#                 res.extend(matrix[i][lef] for i in range(bot, top-1, -1)); lef += 1
#         return res




# direction array simulation chatGPT

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        res = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        x = y = d = 0

        for _ in range(m * n):
            res.append(matrix[x][y])
            visited[x][y] = True
            nx, ny = x + dirs[d][0], y + dirs[d][1]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                x, y = nx, ny
            else:
                d = (d + 1) % 4  # change direction
                x, y = x + dirs[d][0], y + dirs[d][1]
        return res