'''Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.'''






# My logic but not according to question

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i-1])
        return ans
    






# ChatGPT algorithm
# using linear time (O(n)) solution with buckets (as the problem states), we use bucket sort / pigeonhole principle:

# class Solution(object):
#     def maximumGap(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n < 2:
#             return 0
        
#         low, high = min(nums), max(nums)
#         if low == high:
#             return 0

#         size = max(1, (high - low) // (n - 1))
#         bucket_count = (high - low) // size + 1

#         buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

#         for num in nums:
#             idx = (num - low) // size
#             buckets[idx][0] = min(buckets[idx][0], num)
#             buckets[idx][1] = max(buckets[idx][1], num)

#         prev = low
#         ans = 0
#         for bmin, bmax in buckets:
#             if bmin == float('inf'):
#                 continue
#             ans = max(ans, bmin - prev)
#             prev = bmax
#         return ans