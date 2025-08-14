'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]'''






# My logic but not allowed 

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()

# now Using algorithm Merge Sort (Little bit chatGPT)

# class Solution(object):
#     def sortColors(self, nums):
#         if len(nums) <= 1:
#             return

#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]

#         self.sortColors(left)
#         self.sortColors(right)

#         self.merge(left, right, nums)

#     def merge(self, left, right, nums):
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1










# Leetcode best solution

# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         counts = [0]*3
#         for n in nums:
#             counts[n] += 1
#         nums[0:counts[0]] = [0]*counts[0]
#         nums[counts[0]:counts[0]+counts[1]] = [1]*counts[1]
#         nums[counts[0]+counts[1]:counts[0]+counts[1]+counts[2]] = [2]*counts[2]