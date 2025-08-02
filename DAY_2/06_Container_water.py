'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1'''










# My logic but time limit exceeded

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                if area > max_water:
                    max_water = area

        return max_water






# optimized code of above version

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left = 0
#         right = len(height) - 1
#         max_water = 0

#         while left < right:
#             h = min(height[left], height[right])
#             w = right - left
#             area = h * w
#             if area > max_water:
#                 max_water = area

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1

#         return max_water












# Leetcode best solution

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         left=0
#         right=len(height)-1
#         maxarea=0
#         while left<right:
#             minlength=min(height[left], height[right])
#             area=minlength*(right-left)
#             maxarea=max(area, maxarea)
#             if minlength==height[left]:
#                 left+=1
#             else:
#                 right-=1
#         return maxarea

        