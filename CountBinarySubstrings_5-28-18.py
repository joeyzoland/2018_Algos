#leetcode
#https://leetcode.com/problems/count-binary-substrings/description/

#Initialize a digit variable to the first digit of the string
#Initialize count at 1
#Initialize secondDigit at False
#Initialize secondCount at 0
#Initialize solutions at 0
#Iterate through the remainder of the string
    #If the current digit matches the digit variable
        #count += 1
    #Else:
        #If secondDigit does not equal False (meaning that this is not the first time we are seeing a new number, and thus secondDigit actually does have a frequency to compare against)
            #Take the minimum of the firstCount and secondCount, and add it onto the solutions variable
        #Set digit to secondDigit
        #Set count to secondCount
        #Set secondDigit to the current digit
        #Set secondCount to 1
#Check the secondCount against the count one last time, as this won't run when the loop finishes, and do the stuff above
#Return solutions variable

#11001

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        firstCount = 1
        currentDigit = s[0]
        secondCount = 0
        solutions = 0
        for num in s[1:]:
            if (num == currentDigit):
                #If you are on the first iteration, your firstCount is going to be incremented because you don't know how long of a string of the first digit you have; otherwise, you're looking at incrementing secondCount to compare against firstCount; firstCount will keep moving because, when the digit switches, the old secondCount will become firstCount
                if (secondCount == 0):
                    firstCount += 1
                else:
                    secondCount += 1
            else:
                if (secondCount == 0):
                    currentDigit = num
                    secondCount = 1
                else:
                    solutions += min(firstCount, secondCount)
                    firstCount = secondCount
                    currentDigit = num
                    secondCount = 1
        solutions += min(firstCount, secondCount)
        return solutions

ourSolution = Solution()
sample = "00110"
print(ourSolution.countBinarySubstrings(sample))
