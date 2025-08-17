'''Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true'''








# My logic using loop and condition

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         if len(s1) + len(s2) != len(s3):
#             return False

#         m, n = len(s1), len(s2)

#         dp = []
#         for i in range(m + 1):
#             row = []
#             for j in range(n + 1):
#                 row.append(False)
#             dp.append(row)

#         dp[0][0] = True

#         for i in range(m + 1):
#             for j in range(n + 1):
#                 if i > 0 and s1[i-1] == s3[i+j-1] and dp[i-1][j]:
#                     dp[i][j] = True
#                 if j > 0 and s2[j-1] == s3[i+j-1] and dp[i][j-1]:
#                     dp[i][j] = True

#         return dp[m][n]








# Leet code best solution

# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         from collections import Counter

#         if Counter(s3) != Counter(s1 + s2):
#             return False

#         memo={}
#         def dfs(i,j,k):
#             if (i,j,k) in memo:
#                 return memo[(i,j,k)]
#             if k==len(s3):
#                 return True
#             if i!=len(s1):
#                 if s3[k]==s1[i] and dfs(i+1,j,k+1):
#                     memo[i,j,k]=True
#                     return True
#             if j!=len(s2):
#                 if s3[k]==s2[j] and dfs(i,j+1,k+1):
#                     memo[(i,j,k)]=True
#                     return True
#             memo[(i,j,k)]=False
#             return False
#         return dfs(0,0,0)
            