'''Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
'''









# My logic but time limit exceeded

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = nums[0] 
        
        for i in range(n):
            temp_sum = 0
            for j in range(i, n):
                temp_sum += nums[j]   
                if temp_sum > max_sum:
                    max_sum = temp_sum  
        
        return max_sum
    









# Kadane’s Algorithm
'''Keep a running sum (current_sum), adding each element.

If current_sum becomes less than the current element, restart from that element (since starting fresh might give a bigger sum).

Keep track of the max_sum seen so far.'''


# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         msum = nums[0]
#         csum = nums[0]
#         for num in nums[1:]:
#             csum = max(num, csum + num)
#             msum = max(msum, csum)
#         return msum
