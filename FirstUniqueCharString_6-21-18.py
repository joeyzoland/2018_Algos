#https://leetcode.com/problems/first-unique-character-in-a-string/description/



"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.



Diagramming

loveleetcode
^

{l:1, o:1, v:1}...

l has a count of 2, so we keep going
0 has a count of 2, so we keep going
v has a count of 1, so we return it
"""

class Solution:
    def firstUniqChar(self, s):
        myDict = {}
        for char in s:
            if char not in myDict:
                myDict[char] = 1
            else:
                myDict[char] += 1
        for index in range(0, len(s)):
            if (myDict[s[index]] == 1):
                return index
        return -1

mySolution = Solution()
print(mySolution.firstUniqChar("loveleetcode"))
