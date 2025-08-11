'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.'''








# My logic

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort() 
        merged = []

        for i in range(len(intervals)):
            if len(merged) == 0 or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                if intervals[i][1] > merged[-1][1]:
                    merged[-1][1] = intervals[i][1]

        return merged
        







# Algorithm approach
'''Alright — if you want this fully as an algorithm without relying on Python’s built-in sort() trick, we can implement:

Sorting phase → use a simple algorithm like Bubble Sort or Selection Sort to sort intervals by start time.

Merging phase → loop through intervals, merge overlapping ones.'''


# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         n = len(intervals)
#         for i in range(n):
#             min_idx = i
#             for j in range(i + 1, n):
#                 if intervals[j][0] < intervals[min_idx][0]:
#                     min_idx = j
#             intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]

#         merged = []
#         for i in range(n):
#             if len(merged) == 0 or merged[-1][1] < intervals[i][0]:
#                 merged.append(intervals[i])
#             else:
#                 if intervals[i][1] > merged[-1][1]:
#                     merged[-1][1] = intervals[i][1]

#         return merged