#leetcode
#https://leetcode.com/problems/longest-uncommon-subsequence-i/description/

#Test cases:
#aba
#cdaba

#If the lengths between the two input strings are equal:
    #If one equals the other
        #Return -1 (if one string matches the other, then that means all of their possible subsequences match, so there is no uncommon substring)
    #Else
        #Return the length of subsequence a (by definition, the longer the subsequence, the more likely they are to be different, so no need to ever dig into the strings as the entire length is the answer)
#Else if string1 is longer than string2
    #Return string1 (there is no way string1 can be in string2 if string1 is longer, and vice versa)
#Else
    #Return string2

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if(len(a) == len(b)):
            if (a != b):
                return len(a)
            else:
                return -1
        elif (len(a) < len(b)):
            return len(b)
        else:
            return len(a)

ourSolution = Solution()
sampleA = "aba"
sampleB = "cdaba"
print(ourSolution.findLUSlength(sampleA, sampleB))
sampleA2 = "aba"
sampleB2 = "aba"
print(ourSolution.findLUSlength(sampleA2, sampleB2))
sampleA3 = "aba"
sampleB3 = "abc"
print(ourSolution.findLUSlength(sampleA3, sampleB3))
