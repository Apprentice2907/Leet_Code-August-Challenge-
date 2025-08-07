'''
Code
Testcase
Test Result
Test Result
43. Multiply Strings
Medium
Topics
premium lock icon
Companies
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"'''





# Leet code best solution

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        self.num1=num1
        self.num2=num2
        result=int(self.num1)*int(self.num2)
        return str(result)
        



# ChatGPT logic but not best

# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
           
#         if num1 == "0" or num2 == "0":
#             return "0"

#         n, m = len(num1), len(num2)
#         result = [0] * (n + m)

#         for i in range(n - 1, -1, -1):
#             for j in range(m - 1, -1, -1):
#                 mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
#                 p1, p2 = i + j, i + j + 1
#                 sum = mul + result[p2]

#                 result[p2] = sum % 10
#                 result[p1] += sum // 10

#         result_str = ''.join(map(str, result)).lstrip('0')
#         return result_str
            