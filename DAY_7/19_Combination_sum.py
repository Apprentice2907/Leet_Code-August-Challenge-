'''Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []'''








# My logic but chatGPT coded(Backtracking)

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  
                path.pop()  
        backtrack(0, [], 0)
        return result
    




# Another logic using Tabulation

# We create a DP array where dp[i] holds a list of combinations that sum up to i.

# Initialize dp[0] = [[]] because there's one way to make the sum 0: by choosing nothing.

# For every candidate, for every possible sum from that candidate up to target, we update combinations.

# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         dp = [[] for _ in range(target + 1)]
#         dp[0] = [[]]  

#         for num in candidates:
#             for t in range(num, target + 1):
#                 for combination in dp[t - num]:
#                     dp[t].append(combination + [num])

#         return dp[target]
