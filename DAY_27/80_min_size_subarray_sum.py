'''Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0'''






# My logic but time limit exceeded

class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        ans = 10**9

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s >= target:
                    ans = min(ans, j - i + 1)
                    break

        return 0 if ans == 10**9 else ans







# Leet code best solution

# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         if(len(nums)<2):
#             if(nums[0]>=target):
#                 return 1
#             return 0
#         if target == 396893380:
#             return 79517
#         elif target == 1000000000:
#             return 100000
            
#         left = 0
#         curr_sum = 0
#         min_len = float('inf')

#         for right in range(len(nums)):
#             curr_sum += nums[right]

#             while curr_sum >= target:
#                 min_len = min(min_len, right - left + 1)
#                 curr_sum -= nums[left]
#                 left += 1

#         return 0 if min_len == float('inf') else min_len  
            