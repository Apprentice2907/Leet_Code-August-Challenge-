'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 '''









# My logic using simple conditonal 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            rev = -int(str(-x)[::-1])
        else:
            rev = int(str(x)[::-1])

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
    





# Different logic 

# class Solution(object):
#     def reverse(self, x):
#         rx=0
#         neg=0
#         if x<0:
#             neg=1
#             x=abs(x)


#         while x>0:
#             remainder=x%10
#             rx=rx*10+remainder
#             x=x//10
#         if rx>(-2**31) and rx<(2**31-1) and neg==0:
#             return rx
#         elif rx>(-2**31) and rx<(2**31-1) and neg==1:
#             return -rx
#         else:
#             return 0