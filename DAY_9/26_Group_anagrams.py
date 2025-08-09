'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]'''








# My logic but time limit exceeded

# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         result = []
#         while strs:
#             word = strs[0]
#             group = [word]
#             strs = strs[1:]
#             non_anagrams = []
#             for w in strs:
#                 if sorted(w) == sorted(word):
#                     group.append(w)
#                 else:
#                     non_anagrams.append(w)
#             result.append(group)
#             strs = non_anagrams
#         return result
            


# ChatGPT optimized

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        groups = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        
        return list(groups.values())






# Leetcode best logic

# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         anagrams={}
#         for word in strs:
#             key=''.join(sorted(word))
#             if key not in anagrams:
#                 anagrams[key] = []
#             anagrams[key].append(word)
#         return list(anagrams.values())
        