'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"'''







# My logic 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = []
        for _ in range(numRows):
            rows.append("")

        crow = 0
        gdown = False

        for c in s:
            rows[crow] += c
            if crow == 0 or crow == numRows - 1:
                gdown = not gdown
            crow += 1 if gdown else -1

        return ''.join(rows)
            









# Another Logic ChatGPT

# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1 or numRows >= len(s):
#             return s

#         result = ""

#         cycle = 2 * numRows - 2  

#         for row in range(numRows):
#             i = row
#             while i < len(s):
#                 result += s[i]
#                 if row != 0 and row != numRows - 1:
#                     diag = i + cycle - 2 * row
#                     if diag < len(s):
#                         result += s[diag]
#                 i += cycle

#         return result