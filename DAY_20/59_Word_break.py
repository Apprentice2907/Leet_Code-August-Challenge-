'''Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false'''







# My logic simple and easy using slicing

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[0] = True   
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break 
        return dp[n]
    





# Leet code best solution

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: bool
#         """

#         dict_set = set(wordDict)
#         if not dict_set:
#             return False
        
#         max_len = max(len(w) for w in dict_set)


#         n = len(s)
#         dp = [False] * (n + 1)
#         dp[0] = True 

#         for i in range(1, n + 1):
#             for l in range(1, min(max_len, i) + 1):
#                 if not dp[i - l]:
#                     continue
#                 if s[i-l:i] in dict_set:
#                     dp[i] = True
#                     break
#         return dp[n]