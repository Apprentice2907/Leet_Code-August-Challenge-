'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 '''







# My logic but chatGPT coded

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        cand1, cand2, count1, count2 = None, None, 0, 0
        for n in nums:
            if cand1 == n:
                count1 += 1
            elif cand2 == n:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        n_len = len(nums)
        if nums.count(cand1) > n_len // 3:
            res.append(cand1)
        if cand2 is not None and cand2 != cand1 and nums.count(cand2) > n_len // 3:
            res.append(cand2)
        
        return res










# Leetcode best solution

class Solution:
    def majorityElement(self, nums):
        if not nums:
            return []
        
        cand1, cand2, count1, count2 = None, None, 0, 0

        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        n = len(nums)
        if nums.count(cand1) > n // 3:
            result.append(cand1)
        if cand2 != cand1 and nums.count(cand2) > n // 3:
            result.append(cand2)
        
        return result