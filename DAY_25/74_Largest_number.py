'''Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"'''
 





# My logic but chatGPT coded

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = [str(num) for num in nums]

        n = len(nums_str)
        for i in range(n):
            for j in range(i + 1, n):
                if nums_str[i] + nums_str[j] < nums_str[j] + nums_str[i]:
                    nums_str[i], nums_str[j] = nums_str[j], nums_str[i]

        result = ''
        for num in nums_str:
            result = result + num

        if result[0] == '0':
            return '0'
        return result
    







# Leet code best logic

# from functools import cmp_to_key

# class Solution(object):
#     def largestNumber(self, nums):
#         nums_as_str = [str(num) for num in nums]
#         nums_as_str.sort(key=cmp_to_key(self.compare_numbers))

#         if nums_as_str[0] == "0":
#             return "0"
        
#         return "".join(nums_as_str)

#     def compare_numbers(self, a, b):
#         if a + b < b + a:
#             return 1
#         else:
#             return -1