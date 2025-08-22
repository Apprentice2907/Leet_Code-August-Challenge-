'''The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]'''







# My logic using set first creating substring and then checking for occurence

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        seen = set()
        rep = set()

        for i in range(n - 9):  
            subs = s[i:i+10]
            if subs in seen:
                rep.add(subs) 
            else:
                seen.add(subs)
        
        return list(subs)
    






# Leetcode best solution

# class Solution(object):
#     def findRepeatedDnaSequences(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         if(len(s)<10):
#             return []
#         if "GATGGATACTGCATTCGAACCAGAGCCGGCTTTTGCGGGACTAGCATGAGGGACTTG" in s:
#             return []
#         lst={}
#         finlst={}
#         for i in range(0,len(s)-10+1):
#             s1=s[i:i+10]
#             if(s1 in lst):
#                 finlst[s1]=1
#             else:
#                 lst[s1]=1
#         finlst2=[]
#         for i in finlst:
#             finlst2.append(i)
#         return finlst2