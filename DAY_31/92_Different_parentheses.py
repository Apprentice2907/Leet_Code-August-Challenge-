'''Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10'''







# My logic using loop and condition but chatGPT coded

class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            res.append(l + r)
                        elif expression[i] == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)
        if not res:
            res.append(int(expression))
        return res








# Leet code best solution

class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def ways(expr):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    # split into left and right
                    left = ways(expr[:i])
                    right = ways(expr[i+1:])
                    
                    # combine results
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            else:  # '*'
                                results.append(l * r)
            
            # if no operator found, it's just a number
            if not results:
                results = [int(expr)]
            
            memo[expr] = results
            return results

        return ways(expression)