'''Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 

Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
 '''








# My logic using loops and conditions

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        for _ in range(rows + cols):
            if row >= rows or col < 0:
                break
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False
    







# Leet code best solution

class Solution(object):

    def search_recurse(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        mid_m = m/2
        mid_n=  n/2
        # ex) 
        print("mids, ", m,n, mid_m, mid_n, matrix[mid_m][mid_n])

        if target == matrix[mid_m][mid_n]:
            return True
        elif target < matrix[mid_m][mid_n]:
            # recurse in top left
            # print("hereeee", mid_m, mid_n, matrix[:mid_m+1,:mid_n+1])
            top_left = [row[:mid_n+1] for row in matrix[:mid_m+1]]
            print(top_left)
            return self.search_recurse(matrix[0:mid_m+1][0:mid_n+1], target)
        # else:
        #     a = self.search_recurse(matrix[0:mid_m+1][mid_n:-1], target)
        #     b = self.search_recurse(matrix[mid_m:-1][0:mid_n+1], target)
        #     c = self.search_recurse(matrix[mid_m:-1][mid_n:-1], target)
        #     return a & b & c



    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        """ 
        i = 0 # y
        j = len(matrix[0])-1 # x
        while True:
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]: # go left
                if j == 0:
                    return False
                j -=1
            else:
                if i == len(matrix)-1:
                    return False
                i+=1

        return False
        return # self.search_recurse(matrix, target)
        
        