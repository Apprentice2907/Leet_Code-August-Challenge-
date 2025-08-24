'''Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".'''










# mY LOGIC using split and then looping wiht conditions b8ut little bit ChatGPT and
# BEST LEET CODE SOLUTION

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        # v1 = []
        # for x in version1.split("."):
        #     v1.append(int(x))
        
        # v2 = []
        # for x in version2.split("."):
        #     v2.append(int(x))
            
        mlen = max(len(v1), len(v2))
        while len(v1) < mlen:
            v1.append(0)
        while len(v2) < mlen:
            v2.append(0)
        
        for i in range(mlen):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        
        return 0