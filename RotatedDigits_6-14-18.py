#leetcode
#https://leetcode.com/problems/rotated-digits/description/

#15
#Rotated
#12

#Initialize two sets of numbers: rotateValid and rotateNew (respectively, these sets include numbers that rotate to themselves and those that rotate to new numbers)
#Initialize a solutions variable at 0
#Iterate through the range from 1 to N
    #Convert the number to a string
    #Initialize a variable called newNumber = False
    #Initialize a variable called invalid = False
    #Iterate through the digits
        #If the digit is in rotateNew:
            #newNumber = True
            #Continue
        #Else if the digit is in rotateValid:
            #Continue
        #Else (if it's not in either):
            #invalid = true
            #Break (the entire number is invalid)
    #If newNumber == True (there was at least one number that rotated to a new number) and invalid == False (there were no numbers that could not be rotated):
        #solution += 1
#Return solution

#NOTE: Some solutions utilized the fact that you can simply check if there's an invalid number and break the iteration if there is one in the number string; otherwise, you can check if there is one of the rotateNew numbers and then increment the count if there is, since the rotateValid don't actually matter

#NOTE: I bet this could be optimized further by tracking where you find an invalid and incrementing several steps; for example, looking at each number from 41 to 49 is inefficient, since you know all of them will be invalid because they all start with 4, so if there could be some way to increment from 41 to 50...

class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        solutions = 0
        rotateValid = {'0', '1', '8'}
        rotateNew = {'2', '5', '6', '9'}
        for i in range(1, N + 1):
            myString = str(i)
            newNumber = False
            invalid = False
            for digit in myString:
                if (digit in rotateNew):
                    newNumber = True
                    continue
                elif (digit in rotateValid):
                    continue
                else:
                    invalid = True
                    break
            if (newNumber == True and invalid == False):
                solutions += 1
        return solutions

ourSolution = Solution()
sample = 10
print(ourSolution.rotatedDigits(sample))
