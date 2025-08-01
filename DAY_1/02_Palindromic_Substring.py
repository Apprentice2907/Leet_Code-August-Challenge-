'''Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"'''





# My logic using left right variable binary search type but chatGPT coded

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s

        start = 0
        max_len = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
      
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1

        return s[start:start + max_len]
    









# Another Logic

# def longest_palindrome(s):
#     n = len(s)
#     if n == 0:
#         return ""

#     dp = [[False] * n for _ in range(n)]
#     start = 0
#     max_len = 1

#     # Every single character is a palindrome
#     for i in range(n):
#         dp[i][i] = True

#     # Check all substrings of length 2
#     for i in range(n - 1):
#         if s[i] == s[i + 1]:
#             dp[i][i + 1] = True
#             start = i
#             max_len = 2

#     # Check all substrings of length >= 3
#     for length in range(3, n + 1):  # substring length
#         for i in range(n - length + 1):
#             j = i + length - 1  # end index
#             if s[i] == s[j] and dp[i + 1][j - 1]:
#                 dp[i][j] = True
#                 start = i
#                 max_len = length

#     return s[start:start + max_len]
