#LeetCode
#https://leetcode.com/problems/binary-number-with-alternating-bits/description/

#Convert the number to a binary representation string
#Create a prev variable that equals the first character in the string
#Iterate through the rest of the string
    #If the number does not match prev
        #Save the new number to prev
    #If the number matches
        #Return False
#If the loop finishes, return True


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]
        prev = binary[0]
        for i in range(1, len(binary)):
            if (binary[i] == prev):
                return False
            else:
                prev = binary[i]
        return True

ourSolution = Solution()
sampleN = 5
print(bin(sampleN)[2:])
print(ourSolution.hasAlternatingBits(sampleN))
