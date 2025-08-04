'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]'''




# my logic using stack

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        stk = [("", 0, 0)]

        while stk:
            curr, openc, closec = stk.pop()

            if openc == n and closec == n:
                res.append(curr)
                continue

            if openc < n:
                stk.append((curr + "(", openc + 1, closec))

            if closec < openc:
                stk.append((curr + ")", openc, closec + 1))

        return res
            











# Leetcode best solution

# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         result = []
        
#         def backtrack(current, open_count, close_count):

#             if len(current) == 2 * n:
#                 result.append(current)
#                 return

#             if open_count < n:
#                 backtrack(current + '(', open_count + 1, close_count)
            
#             if close_count < open_count:
#                 backtrack(current + ')', open_count, close_count + 1)

#         backtrack("",0,0)
#         return result