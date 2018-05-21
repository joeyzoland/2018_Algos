#leetcode
#https://leetcode.com/problems/letter-case-permutation/description/

#For each character in a string, we need to return two copies: one in which the letter is lowercase, and one in which it is uppercase

#[a1b]
# ^
#["a", "A"]

#[a1b]
#  ^
#["a1", "A1"]

#[a1b]
#   ^
#["a1b", "A1b", "a1B", "A1B"]

#Initialize a solutions array
#Iterate through the given string
    #If there are no entries in the solution array
        #If it is a number
            #Append the number to the solutions array
        #Else
            #Append two copies of the letter to the solutions array, one uppercase and one lowercase
    #Else (if there is at least one entry)
        #If it is a number
            #Iterate through all entries in the solution array, and append the number to them
        #If it is a character
            #Iterate through all entries in the solution array
                #Create a copy of the entry, add an uppercase letter to the end of it, and append that entry to the solutions array
                #Add the lowercase character to the entry you are looking at
#Return the solutions array

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if (len(S) == 0):
            return [""]
        solutionsArray = []
        #.isalpha returns False if it's a number, and True if it's a letter
        if (S[0].isalpha() == False):
            solutionsArray.append(S[0])
        else:
            solutionsArray.append(S[0].lower())
            solutionsArray.append(S[0].upper())
        for i in range(1, len(S)):
            if (S[i].isalpha() == False):
                for j in range(0, len(solutionsArray)):
                    solutionsArray[j] = solutionsArray[j] + S[i]
            else:
                for j in range(0, len(solutionsArray)):
                    solutionsArray.append(solutionsArray[j] + S[i].upper())
                    solutionsArray[j] = solutionsArray[j] + S[i].lower()
        return solutionsArray

ourSolution = Solution()
sampleString = "a1b2"
print(ourSolution.letterCasePermutation(sampleString))
