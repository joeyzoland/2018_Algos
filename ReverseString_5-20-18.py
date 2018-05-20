#LeetCode
#https://leetcode.com/problems/reverse-string/description/

#Iterate through the string and take the last letter, throw it between the sorted and unsorted letters, then continue
#After the loop, return the input

#hello
#ohell
#olhel
#ollhe
#olleh

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(0, len(s) - 1):
            s = s[:i] + s[-1] + s[i:-1]
        return s

ourSolution = Solution()
print(ourSolution.reverseString("hello"))
