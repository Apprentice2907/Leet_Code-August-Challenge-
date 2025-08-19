'''Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]'''






# My logic using string slicing best logic 97%

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]
        
        for i in range(1, n + 1):
            for j in range(i):
                temp = s[j:i]
                if temp == temp[::-1]:
                    for prev in dp[j]:
                        dp[i].append(prev + [temp])
        
        return dp[n]
    




# Leet code best logic which is 100%

# class Solution(object):
#     def isParalind(self,s):
#         if s==s[::-1]:
#             return True
#         return False
    
#     def backtracking(self,s,start,dp):
#         if start>=len(s):
#             return [[]]
#         if start in dp:
#             return dp[start]
#         n=len(s)
#         res=[]
#         for i in range(start,n,1):
#             cur=s[start:i+1]
#             if self.isParalind(cur)==False:
#                 continue
#             temp=self.backtracking(s,i+1,dp)
#             for item in temp:
#                 res.append([cur]+item)
#         dp[start]=res
#         return res

#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         dp={}
#         res=self.backtracking(s,0,dp)
#         return res