#leetcode
#https://leetcode.com/problems/most-common-word/description/

#"Bob hit a ball, the hit BALL flew far after it was hit."

#Initialize firstLetter = False
#Initialize a hashMap = {}
#Iterate through the paragraph
    #If the character is a letter
        #If there is currently no first letter recorded:
            #firstLetter = your current index
        #Else
            #continue (i.e., do nothing)
    #Else (if the character is not a letter)
        #If there was a first letter that does not equal false
            #Set a word variable, from firstLetter to preceding index i, that is all lowercase
            #Set a variable, bannedFlag = False
            #Iterate through the banned list
                #If that word is in the banned list
                    #bannedFlag = True
                    #Break
            #If banned == True
                #Break
            #If that word was not in hashMap (and is not banned)
                #Add it to hashMap with value 1
            #else
                #Add 1 to its frequency
#Initialize currentWord
#Initialize frequency at 0
#Iterate through hashMap
    #If the value is greater than frequency
        #currentWord = the key you are looking at
        #frequency = that key's frequency
#Return currentWord

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        firstLetter = "NA"
        hashMap = {}
        for i in range(0, len(paragraph)):
            if (paragraph[i].isalpha() == True):
                if (firstLetter == "NA"):
                    firstLetter = i
                else:
                    continue
            else:
                if (firstLetter != "NA"):
                    word = paragraph[firstLetter:i].lower()
                    #Resetting firstLetter since we know we are on a non-letter space
                    firstLetter = "NA"
                    #This is assuming that all banned words are lowercase
                    if (word in banned):
                        continue
                    if (word not in hashMap):
                        hashMap[word] = 1
                    else:
                        hashMap[word] += 1
        #We have to check one more time, in case the paragraph doesn't end with punctuation and ends with a word instead
        if (firstLetter != "NA"):
            word = paragraph[firstLetter:].lower()
            #Resetting firstLetter since we know we are on a non-letter space
            firstLetter = "NA"
            if (word not in hashMap and word not in banned):
                hashMap[word] = 1
            elif (word not in banned):
                hashMap[word] += 1
        currentWord = hashMap.keys()[0]
        frequency = hashMap[hashMap.keys()[0]]
        for key in hashMap.keys()[1:]:
            if (hashMap[key] > frequency):
                currentWord = key
                frequency = hashMap[key]
        return currentWord

ourSolution = Solution()
sampleParagraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(ourSolution.mostCommonWord(sampleParagraph, banned))
