'''Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.'''





# My logic simple and easy 

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        cmax = nums[0]
        cmin = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                cmax, cmin = cmin, cmax
            cmax = max(n, cmax * n)
            cmin = min(n, cmin * n)
            res = max(res, cmax)
        return res
            





# Leet code best solution

# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         pre,suffix = 1,1
#         ans= float('-inf')
#         for i in range(n):
#             if pre == 0:
#                 pre = 1
#             if suffix ==0:
#                 suffix = 1
#             pre*=nums[i]
#             suffix *= nums[n-i-1]
#             ans = max(ans,pre,suffix)
#         return ans