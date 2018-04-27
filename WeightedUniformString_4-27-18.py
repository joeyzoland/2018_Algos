#https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#Note: The above section of code worked, but it didn't make time requirements, but the second one does

# def weightedUniformStrings(s, queries):
#     weightedAlphabet = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
#
#     objectHolder = {}
#     loopCounter = 0
#     while (loopCounter < len(s)):
#         if (weightedAlphabet[s[loopCounter]] not in objectHolder.keys()):
#             objectHolder[weightedAlphabet[s[loopCounter]]] = True
#         #Check if the current letter is the last letter in s; if it is, you don't need to check for consecutive duplicates
#         if (loopCounter == len(s) - 1):
#             break
#         consecutiveCounter = 1
#         while (s[loopCounter + consecutiveCounter] == s[loopCounter]):
#             if (weightedAlphabet[s[loopCounter]] * (consecutiveCounter + 1) not in objectHolder.keys()):
#                 objectHolder[weightedAlphabet[s[loopCounter]] * (consecutiveCounter + 1)] = True
#             consecutiveCounter += 1
#             #Check if the current letter is the last letter in s; if it is, you don't need to check for consecutive duplicates
#             if (loopCounter + consecutiveCounter == len(s)):
#                 break
#         loopCounter += consecutiveCounter
#     for query in queries:
#         if (query in objectHolder.keys()):
#             print ("Yes")
#         else:
#             print ("No")
#
#     Note: The below code can be used to adapt this to HackerRank's format (it said it wanted each evaluation to print, but it actually wants the solution in an array form)
#
#     solutionsList = []
#     for query in queries:
#         if (query in objectHolder.keys()):
#             solutionsList.append("Yes")
#         else:
#             solutionsList.append("No")
#     return solutionsList



def weightedUniformStrings(s, queries):
    loopCounter = 0
    currentSet = set()
    while (loopCounter < len(s)):
        #Ord gives a value to a letter that is always greater than 96, i.e. a = 97 and b = 98, so we subtract 96 to get the weight and then record that
        if ((ord(s[loopCounter]) - 96) not in currentSet):
            currentSet.add(ord(s[loopCounter]) - 96)
        #Check if the current letter is the last letter in s; if it is, you don't need to check for consecutive duplicates
        if (loopCounter == len(s) - 1):
            break
        consecutiveCounter = 1
        while (s[loopCounter + consecutiveCounter] == s[loopCounter]):
            consecutiveCounter += 1
            if (((ord(s[loopCounter]) - 96) * consecutiveCounter) not in currentSet):
                currentSet.add(((ord(s[loopCounter]) - 96) * consecutiveCounter))
            #Check if the current letter is the last letter in s; if it is, you don't need to check for consecutive duplicates
            if (loopCounter + consecutiveCounter == len(s)):
                break
        loopCounter += consecutiveCounter
    solutionsList = []
    for query in queries:
        if (query in currentSet):
            solutionsList.append("Yes")
        else:
            solutionsList.append("No")
    return solutionsList


# sampleString = "aacee"
# sampleArray = [1, 2, 3, 4, 5, 9, 10]
sampleString = "abccddde"
sampleArray = [1, 3, 12, 5, 9, 10]

print(weightedUniformStrings(sampleString, sampleArray))
