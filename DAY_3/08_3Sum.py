'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.'''







# My logic but ofc time limit reached

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        result = []

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
        return result
    







# Leet code best solution

# class Solution(object):
#     def threeSum(self, nums):
#         res = []
#         nums.sort()
#         for i in range(len(nums)):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             j = i+1
#             k = len(nums)-1

#             while j < k:
#                 total = nums[i] + nums[j] + nums[k]
                
#                 if total> 0:
#                     k-=1
#                 elif total< 0:
#                     j+=1
#                 else:
#                     res.append([nums[i], nums[j], nums[k]])
#                     j+=1

#                     while nums[j] == nums[j-1] and j < k:
#                         j+= 1

#         return res