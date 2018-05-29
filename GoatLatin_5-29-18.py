#LeetCode
#https://leetcode.com/problems/goat-latin/description/

#Convert the sentence into an array of words
#Iterate through the words
    #If it starts with a consonant
        #Cut the first letter off the front and add it to the end
    #Initialize a suffix variable with "ma"
    #Run a range loop starting at 0 and going until word index + 1
        #At each iteration, add an "a" to suffix
    #Add the suffix onto the word
#Join the words back into a string

#"I am great"

#["I", "am", "great"]

#["Ima", "amma", "reatgma"]
#["Imaa", "ammaaa", "reatgmaaaa"]

#"Imaa ammaaa reatgmaaaa"

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowelSet = {"a", "e", "i", "o", "u"}
        myArray = S.split(" ")
        for i in range(0, len(myArray)):
            if (myArray[i][0].lower() not in vowelSet):
                myArray[i] = myArray[i][1:] + myArray[i][0]
            suffix = "ma"
            for j in range(0, i + 1):
                suffix += "a"
            myArray[i] += suffix
        return " ".join(myArray)


ourSolution = Solution()
ourString = "I am great"
print(ourSolution.toGoatLatin(ourString))
