#https://leetcode.com/problems/add-strings/description/

"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.



'11' + '99' -> 110

add 1's digits first to get 10, then multiply by 10^0 to get 10

add 2's digits next to get 10, then multiply by 10^1, then add onto previous to get 100
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        counter = 0
        sum = 0
        #numDict is used for converting string digits to numbers
        numDict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        #numList is for converting numbers to string digits
        numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        #If there are digits left in both strings, use this loop to convert them to numbers and add them together
        while counter < len(num1) and counter < len(num2):
            num1Digit = num1[len(num1) - 1 - counter]
            num2Digit = num2[len(num2) - 1 - counter]
            current = numDict[num1Digit] + numDict[num2Digit]
            #Multiplying by 10 to the power of counter allows us to convert the digit back to its rightful place, e.g., a 2 in the ten's place becomes 20
            current *= 10**counter
            sum += current
            counter += 1
        #If there's just digits left in num1
        while counter < len(num1):
            num1Digit = num1[len(num1) - 1 - counter]
            current = numDict[num1Digit]
            current *= 10**counter
            sum += current
            counter += 1
        #If there's just digits left in num2
        while counter < len(num2):
            num2Digit = num2[len(num2) - 1 - counter]
            current = numDict[num2Digit]
            current *= 10**counter
            sum += current
            counter += 1

        if sum == 0:
            return "0"
        result = ""
        #This iterates through each digit in sum from the back and converts each to a string, then adds it onto the front of the existing result string, and finally removes that digit from sum
        while sum > 0:
            currentDigit = sum % 10
            result = numList[currentDigit] + result
            sum -= currentDigit
            sum /= 10
        return result

mySolution = Solution()
print(mySolution.addStrings("9133", "68"))
