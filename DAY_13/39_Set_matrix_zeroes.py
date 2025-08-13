'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]'''








# My logic using set function

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r, c = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in r or j in c:
                    matrix[i][j] = 0







# Leet code best solution

# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         def SetRowZero(row):
#             for i in range(n):
#                 if(matrix[row][i]==0):
#                     continue
#                 matrix[row][i] = "$"
        
#         def SetColZero(col):
#             for i in range(m):
#                 if(matrix[i][col]==0):
#                     continue
#                 matrix[i][col] = "$"
                
#         m, n = len(matrix), len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if(matrix[i][j]==0):
#                     SetRowZero(i)
#                     SetColZero(j)
#         for i in range(m):
#             for j in range(n):
#                 if(matrix[i][j]=="$"):
#                     matrix[i][j] = 0