#LeetCode
#https://leetcode.com/problems/find-the-difference/description/

#Sort both lists
#Check each character between lists
    #If there is not a match, return the character in string "t"
#If the loop completes, return the last character of "t" because it must be the new one

#abd
#bacd

#After Sort
#abd
#abcd


#abd
#abcd
#^

#abd
#abcd
# ^

#abd
#abcd
#  ^

#Return c

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return t[i]
        #If the for loop completes without finding a mismatch, then the new character must be at the end of string "t"
        return t[-1]

ourSolution = Solution()
sampleString1 = "abd"
sampleString2 = "cabd"
print(ourSolution.findTheDifference(sampleString1, sampleString2))
