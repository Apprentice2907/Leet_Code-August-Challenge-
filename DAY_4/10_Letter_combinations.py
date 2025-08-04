'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]'''







# My logic using dictionary mapping and 100% runtime

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = [""]

        for digit in digits:
            if digit not in phone:
                continue

            temp = []
            for pre in result:
                for letter in phone[digit]:
                    temp.append(pre + letter)
            result = temp

        return result
            








# Leet code logic 

# class Solution(object):
#     def backtrack(self,index, current, digits, phoneMap, result):
#         if index == len(digits):
#             result.append(current)
#             return
        
#         letters = phoneMap[digits[index]]
#         for letter in letters:
#             self.backtrack(index + 1, current + letter, digits, phoneMap, result)
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if not digits:
#             return []
    
#         # Mapping of digits to corresponding letters
#         phoneMap = {'0':'','1':'',
#             '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
#             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
#         }

    

#         result = []
#         self.backtrack(0, "",digits,phoneMap,result)
#         return result
        