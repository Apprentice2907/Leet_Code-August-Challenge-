'''A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
'''







# ChatGPT as i dont understand how to solve this 
# Best solution

class Solution(object):
    def restoreIpAddresses(self, s):
        n = len(s)
        res = []
        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if (str(int(a)) == a and 0 <= int(a) <= 255 and
                        str(int(b)) == b and 0 <= int(b) <= 255 and
                        str(int(c)) == c and 0 <= int(c) <= 255 and
                        str(int(d)) == d and 0 <= int(d) <= 255):
                        res.append(a + "." + b + "." + c + "." + d)
        return res
