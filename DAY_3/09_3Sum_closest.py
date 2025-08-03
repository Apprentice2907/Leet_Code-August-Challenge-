'''Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).'''










# My logic but time limit reached

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        mdiff = 10**9
        cnum = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = nums[i] + nums[j] + nums[k]
                    d = abs(s - target)
                    if d < mdiff:
                        mdiff = d
                        cnum = s

        return cnum
    


# Optimized code given by chatGPT

# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         nums.sort()
#         n = len(nums)
#         mdiff = 10**9
#         cnum = 0

#         for i in range(n - 2):
#             l = i + 1
#             r = n - 1

#             while l < r:
#                 s = nums[i] + nums[l] + nums[r]
#                 d = abs(s - target)

#                 if d < mdiff:
#                     mdiff = d
#                     cnum = s

#                 if s < target:
#                     l += 1
#                 else:
#                     r -= 1

#         return cnum