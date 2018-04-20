#https://www.hackerrank.com/challenges/two-characters/problem

"""
In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.
"""

def twoCharacters(s):
    if (s is None):
        return None
    #letterList translates s from a string into an array of individual characters, and then sorts them
    letterList = []
    for letter in s:
        letterList.append(letter)
    letterList.sort()
    #nonDuplicated takes the individual characters from letterList, and becomes a list that has only one copy of each letter
    nonDuplicated = [letterList[0]]
    for i in range(1, len(letterList)):
        if (letterList[i] != letterList[i - 1]):
            nonDuplicated.append(letterList[i])
    maxLength = 0
    #After choosing two characters from the nonDuplicated list, this finds the first instance of one of the two letters.  If the first of the two letters found is the first letter with index "a", firstCharacterLast = True to record that the one with index "a" was the last recorded; the opposite goes for if the one with index "b" was found first.  Afterwards, if there is a repeat of the same letter, we know to break the sequence and not record it by changing the endedEarly flag to True.  However, if it's the alternative letter, we update currentCount by 1 and firstCharacterLast.  Assuming the entire two-character string wasn't invalid, we compare the length of our current two-character string against the longest previous one, and if it's longer, we record it.  At the end, we simply print out the maximum length.
    for a in range(0, len(nonDuplicated) - 1):
        for b in range(a + 1, len(nonDuplicated)):
            currentCount = 0
            firstCharacterLast = None;
            endedEarly = False
            for character in s:
                if (firstCharacterLast is None):
                    if (character == nonDuplicated[a]):
                        firstCharacterLast = True
                        currentCount += 1
                    elif (character == nonDuplicated[b]):
                        firstCharacterLast = False
                        currentCount += 1
                else:
                    if (character == nonDuplicated[a]):
                        if (firstCharacterLast == True):
                            endedEarly = True
                            break
                        else:
                            firstCharacterLast = True
                            currentCount += 1
                    elif (character == nonDuplicated[b]):
                        if (firstCharacterLast == False):
                            endedEarly = True
                            break
                        else:
                            firstCharacterLast = False
                            currentCount += 1
            if (endedEarly == False):
                if (currentCount > maxLength):
                    maxLength = currentCount
    return maxLength

print (twoCharacters("cheshee"))
