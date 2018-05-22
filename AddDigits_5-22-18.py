#leetcode
#https://leetcode.com/problems/add-digits/description/

#Save the input to a solution variable
#While the solution variable is greater than 10
    #Convert the solution variable to a string
    #Create a sum variable
    #Iterate through the solution string and add all of them to sum
    #Save sum to solution
#After the while loop is done (i.e., less than 10), return it

#38

#3 + 8 = 11

#1 + 1 = 2

#Return 2




class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        solution = num
        while (solution > 9):
            stringSolution = str(solution)
            sum = 0
            for char in stringSolution:
                sum += int(char)
            solution = sum
        return solution

ourSolution = Solution()
sampleNumber = 38
print(ourSolution.addDigits(38))
