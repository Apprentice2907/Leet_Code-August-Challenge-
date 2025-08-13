'''Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')'''











# My logic 

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            dp.append(row)

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert_op = dp[i][j - 1] + 1
                    delete_op = dp[i - 1][j] + 1
                    replace_op = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(insert_op, delete_op, replace_op)

        return dp[m][n]
    










# Leetcode best solution

# class Solution(object):
#     def minDistance(self, word1, word2):
#         rows = len(word1)+1
#         cols = len(word2)+1

#         costdp = [[0 for _ in range(cols)] for _ in range(rows)]
#         for i in range(rows):
#             costdp[i][0] = i
#         for i in range(cols):
#             costdp[0][i] = i
#         for i in range(1,rows):
#             for j in range(1,cols):
#                 if word1[i-1] == word2[j-1]:
#                     costdp[i][j] = costdp[i-1][j-1]
#                 else:
#                     costdp[i][j] = min(costdp[i-1][j-1],costdp[i-1][j],costdp[i][j-1]) + 1
#         return costdp[len(word1)][len(word2)]