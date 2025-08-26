'''Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0'''





# My logic using for loop and condition but time limit exceeded

class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0

        count = 0
        for num in range(2, n):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return count








# Logic Using Sieve of Eratosthenes

# class Solution(object):
#     def countPrimes(self, n):
#         if n < 3:
#             return 0
#         is_prime = [True] * n
#         is_prime[0] = is_prime[1] = False
#         for i in range(2, int(n**0.5) + 1):
#             if is_prime[i]:
#                 for j in range(i * i, n, i):
#                     is_prime[j] = False
#         return sum(is_prime)
    




# Leet code best solution

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
# class Solution(object):
#     def countPrimes(self, n):
#         if n <= 2:
#             return 0
        
#         is_prime = [True] * n
#         is_prime[0] = is_prime[1] = False

#         p = 2
#         while p * p < n:
#             if is_prime[p]:
#                 for multiple in range(p * p, n, p):
#                     is_prime[multiple] = False
#             p += 1

#         return sum(is_prime)