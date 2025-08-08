'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]'''





# My logic most common and simple using recursion

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
    






# ChatGPT logic using Heap Algorithm 


# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         n = len(nums)
#         result = []
#         c = [0] * n
#         result.append(nums[:])
#         i = 0
#         while i < n:
#             if c[i] < i:
#                 if i % 2 == 0:
#                     nums[0], nums[i] = nums[i], nums[0]
#                 else:
#                     nums[c[i]], nums[i] = nums[i], nums[c[i]]
#                 result.append(nums[:])
#                 c[i] += 1
#                 i = 0
#             else:
#                 c[i] = 0
#                 i += 1
#         return result