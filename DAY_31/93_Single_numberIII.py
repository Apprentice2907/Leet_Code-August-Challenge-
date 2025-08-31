'''Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]'''







# My logic using loop but time limit exceeded

class Solution(object):
    def singleNumber(self, nums):
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                res.append(nums[i])
        return res







# Leet code best solution using chatGPT

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_all = 0
        for num in nums:
            xor_all ^= num

        diff = xor_all & -xor_all  
        a, b = 0, 0

        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return [a, b]
