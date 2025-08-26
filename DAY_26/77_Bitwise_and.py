'''Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 '''






# My Logic using simple binary but memory exceeded

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        result = left
        for num in range(left + 1, right + 1):
            result = result & num
            if result == 0:
                break
        return result





# Using bit operators

# class Solution(object):
#     def rangeBitwiseAnd(self, left, right):
#         shift = 0
#         while left < right:
#             left >>= 1
#             right >>= 1
#             shift += 1
#         return left << shift







# Leetcode solution

# class Solution(object):
#     def rangeBitwiseAnd(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         while right > left:
#             right = right & (right - 1)
#         return right