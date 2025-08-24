'''Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 '''








# My logic simple but not effiecienct as time limit reached

class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]








# Using binary search logic 

# class Solution(object):
#     def twoSum(self, numbers, target):
#         left = 0
#         right = len(numbers) - 1
        
#         while left < right:
#             current_sum = numbers[left] + numbers[right]
            
#             if current_sum == target:
#                 return [left + 1, right + 1]
#             elif current_sum < target:
#                 left += 1
#             else:
#                 right -= 1









# Leetcode best solution

# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         idx1, idx2 = 0, len(numbers) - 1
#         while idx1 < idx2:
#             cur_sum = numbers[idx1] + numbers[idx2]
#             if cur_sum == target:
#                 return [idx1+1, idx2+1]
#             elif cur_sum > target:
#                 idx2 -= 1
#             else:
#                 idx1 += 1
        
#         assert False
        