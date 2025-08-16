'''Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]'''









# My logic using for loop and condition

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        start = 0
        end = 0

        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1
            end = len(result) - 1
            for j in range(start, len(result)):
                result.append(result[j] + [nums[i]])
        return result







# Recursive logic and using backtracking logic

# class Solution(object):
#     def subsetsWithDup(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()  
#         result = []

#         def backtrack(start, path):
#             result.append(path[:])  
#             for i in range(start, len(nums)):
               
#                 if i > start and nums[i] == nums[i - 1]:
#                     continue
#                 path.append(nums[i])
#                 backtrack(i + 1, path)
#                 path.pop()

#         backtrack(0, [])
#         return result