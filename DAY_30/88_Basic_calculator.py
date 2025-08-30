'''Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5'''









# My logic using stack and enumeration

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign = '+'
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    if stack[-1] < 0:
                        stack[-1] = - (abs(stack[-1]) // num)
                    else:
                        stack[-1] = stack[-1] // num
                
                sign = ch
                num = 0
        
        return sum(stack)










# Leetcode best solution

class Solution(object):
    def calculate(self, s):
        stack, num, sign = [], 0, '+'
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + ord(c) - 48
            elif c == ' ':
                continue
            else:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                else:
                    stack[-1] = int(float(stack[-1]) / num)
                sign, num = c, 0
        return sum(stack)