'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false'''








# My logic and coded by me too😂 best logic 

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for lst in matrix:
            for ele in lst:
                if ele == target:
                    return True
        return False










# My logic but merging the sublist and then performing binary search 

# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         nums = []
#         for row in matrix:
#             for num in row:
#                 nums.append(num)

#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return False








# Leet code logic but worst too

# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
        
#         # firstly find the row
#         start_row = 0
#         end_row = len(matrix) -1
#         mid_row = -1

#         if target < matrix[start_row][0] :
#             # cant be possible if even lower than start
#             return False

#         while end_row >= start_row :

#             mid_row = ( start_row + end_row )//2
#             print(start_row , mid_row, end_row)
#             next_row_exists = mid_row + 1 < len(matrix)

#             # check if element in current mid row
#             if matrix[mid_row][0] < target and next_row_exists and matrix[mid_row+1][0] > target :
#                 break

#             if target < matrix[mid_row][0] :
#                 end_row = mid_row -1
#             elif target > matrix[mid_row][0] :
#                 start_row = mid_row + 1
#             else :
#                 return True

#             print(start_row , mid_row, end_row)
#         # now check in mid_row ROW

#         start_clm = 0
#         end_clm = len(matrix[mid_row]) - 1
#         mid_clm = -1

#         while start_clm <= end_clm :

#             mid_clm = (start_clm + end_clm)//2
#             if matrix[mid_row][mid_clm] > target :
#                 end_clm = mid_clm - 1
#             elif matrix[mid_row][mid_clm] < target :
#                 start_clm = mid_clm + 1
#             else :
#                 return True
#         # print(mid_row , mid_clm)
#         return False