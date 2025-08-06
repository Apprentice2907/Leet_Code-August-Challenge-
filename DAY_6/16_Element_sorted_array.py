'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]'''






# user defined and recursive logic

# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         def find(pos):
#             l, r = 0, len(nums) - 1
#             res = -1
#             while l <= r:
#                 m = (l + r) // 2
#                 if nums[m] == target:
#                     res = m
#                     if pos == "first":
#                         r = m - 1
#                     else:
#                         l = m + 1
#                 elif nums[m] < target:
#                     l = m + 1
#                 else:
#                     r = m - 1
#             return res

#         return [find("first"), find("last")]









# Least line count in leetcode

# class Solution(object):
#     def searchRange(self, arr, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n = len(arr)
#         sub = []
        

#         for i in range (n):
#             if arr[i] == target :
#                 sub.append(i)
        
#         l = len(sub)

#         if l == 0:
#             return [-1,-1]
#         elif l == 1:
#             return sub[0],sub[0]
#         elif l >= 2 :
#             return min(sub),max(sub)



        


# Leetcode another code 

# class Solution(object):
#     def searchRange(self, nums, target):
#         def firstOcc():
#             first=-1
#             low,high=0,len(nums)-1
#             while low<=high:
#                 mid=(low+high)//2
#                 if target==nums[mid]:
#                     first=mid
#                     high=mid-1
#                 elif target>nums[mid]:
#                     low=mid+1
#                 elif target>nums[mid]:
#                     low=mid+1
#                 elif target<nums[mid]:
#                     high=mid-1 
#             return first
#         def lastOcc():
#             last=-1
#             low,high=0,len(nums)-1
#             while low<=high:
#                 mid=(low+high)//2
#                 if target==nums[mid]:
#                     last=mid
#                     low=mid+1
#                 elif target>nums[mid]:
#                     low=mid+1
#                 elif target<nums[mid]:
#                     high=mid-1
#             return last
#         return(firstOcc(),lastOcc())                    

      


        