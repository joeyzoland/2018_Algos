"""
https://leetcode.com/problems/rotate-string/description/

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Weird edge case is that last letter of input should be followed by first char, for both input string and target string
'abcde',     destination -> "cdeab"
   ^
"cdeab"
 ^

Pointer1 in for loop, starting at target string first and iterating through all characters but the last one
    Pointer2 starting at same character of input string (if not there, invalid)
        Grab next characters for both strings (If pointer2 is at the end of the string, next = first characterof the string)

        If next characters match, change the second pointer to next; else, return False
Return True

"""

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True
        char = B[0]
        possibleStarts = []
        for i in range(0, len(A)):
            if A[i] == char:
                possibleStarts.append(i)
                findFlag = True
        if (len(possibleStarts) == 0):
            return False
        for i in possibleStarts:
            secondPointer = i
            matchFlag = True
            for char in B[1:len(B)]:
                if (secondPointer + 1 >= len(A)):
                    secondPointer = 0
                else:
                    secondPointer += 1
                if char != A[secondPointer]:
                    matchFlag = False
                    break
            if matchFlag == True:
                return True
        return False

mySolution = Solution()
print(mySolution.rotateString("abcde", "cdeab"))
print(mySolution.rotateString("abcde", "abced"))

sampleString1 = "vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg"
sampleString2 = "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"
print(mySolution.rotateString(sampleString1, sampleString2))
