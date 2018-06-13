#leetcode
#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/


#Initialize a solutions variable
#Iterate through the range of l to r (inclusive!)
    #Convert each number to it's binary form
    #Convert the binary to a string
    #Initialize a count variable
    #Iterate through the string
        #Every time there is a 1, add 1 to the count variable
    #Make a variable called prime = True
    #Make a for loop starting at 2, through the count variable (noninclusive)
        #At each iteration, break if the count variable % the number == 0 (i.e., the number divides evenly), and set prime variable to False
    #If the prime variable is true (i.e., for loop finished w/ no catch)
        #Increment the solutions variable
#Return the solutions variable

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        solutions = 0
        for i in range(L, R + 1):
            binaryString = str(bin(i)[2:])
            oneCount = 0
            for digit in binaryString:
                if (digit == '1'):
                    oneCount += 1
            #A number with 1 bit cannot be prime because 1 is not prime, so we go onto the next number
            if (oneCount == 1):
                continue
            prime = True
            for num in range(2, oneCount):
                if (oneCount % num == 0):
                    prime = False
                    break
            if (prime == True):
                solutions += 1
        return solutions

ourSolution = Solution()
sampleL = 6
sampleR = 10
print(ourSolution.countPrimeSetBits(sampleL, sampleR))
