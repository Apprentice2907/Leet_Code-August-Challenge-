'''Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 '''








# My logic using set logic 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        mlen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            mlen = max(mlen, right - left + 1)

        return mlen



# My logic using for looping

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         mlen = 0

#         for i in range(n):
#             temp = 0
#             for j in range(i, n):
#                 duplicate = False
#                 for k in range(i, j):
#                     if s[k] == s[j]:
#                         duplicate = True
#                         break
#                 if duplicate:
#                     break
#                 temp += 1
#             if temp > mlen:
#                 mlen = temp

#         return mlen
            