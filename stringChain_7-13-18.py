"""
https://blog.cancobanoglu.net/2016/09/18/interview-questions-string-chain/

{"a", "b", "ba", "bca", "bda", "bdca"}

Iterate through input set, creating key-value pairs for each word and its length, with matching lengths in the same array; record the biggest bucket
{1:{"a", "b"}, 2:{"ba"}, 3:{"bca", "bda"}, 4:{"bdca"}
Note: This is a map of sets

make a solution variable
record everything you visit in a set
record that you started at the 4 bucket

-start at "bcda" because it's longest, record that you've visited it in your visited set, then look at 3 bucket
-check every word in 3 bucket and, if at least 1 can be traversed that is not in visited, flip a flag saying that this is not the greatest length, and call the function again
-Note, for the above step, if that flag is not flipped, then you're going to want to subtract the word length of the current bucket from your starting point and record it in your global solution variable
-Note that you'll also want to break the function if your solution at any point is greater than the bucket length that you're currently looking at

-After iterating through the entire input set, return the solution
"""
from math import inf
def stringChain(wordSet):
    lengthMap = {}
    visited = set()
    maxLength = -inf
    minLength = inf
    for word in wordSet:
        length = len(word)
        if length not in lengthMap:
            lengthMap[length] = set()
            lengthMap[length].add(word)
            if length > maxLength:
                maxLength = length
            if length < minLength:
                minLength = length
        else:
            lengthMap[length].add(word)
    #The above code creates a map that looks something like this, where the hash keys are the lengths and the values are sets containing words of those given length:
    #{1:{"a", "b"}, 2:{"ba"}, 3:{"bca", "bda"}, 4:{"bdca"}

    solution = -inf
    def stringHelper(word):
        print("on start, word is", word)
        #Because we're working from largest to smallest, if we've already visited the word, we don't have to check it because we know we've already gotten the longest string from that word; if we haven't visited, we add it to visited here and then continue
        if word in visited:
            return
        visited.add(word)

        #If there's no bucket that has words that are one less than the given word's length, then we know there are no possible paths to traverse and thus the path is invalid
        valid = True
        if (len(word) - 1) not in lengthMap:
            valid = False

        #If the path is valid, then we use the variable traversed to verify whether this is the last stop for this particular chain; if it is the last stop, then and only then will we want to check its length against the recorded solution to see if it's bigger
        traversed = False
        if valid == True:
            #Have to check all of the words that can be made by subtracting one letter and, if they are in the input, recursively call on those subWords
            for index in range(0, len(word)):
                nonlocal solution
                if (len(currentWord) - minLength + 1) <= solution:
                    break
                subWord = word[:index] + word[index + 1:]
                print("subWord is", subWord)
                if subWord in lengthMap[len(subWord)] and subWord not in visited:
                    traversed = True
                    stringHelper(subWord)
        #If we didn't traverse down any string chain paths, then we know this solution is the longest for this chain and thus can be checked against the recorded solution to see if it's bigger
        if traversed == False:
            possibleSolution = currentLength - len(word) + 1
            if possibleSolution > solution:
                solution = possibleSolution
            #NOTE TO SELF: PROBABLY NEED TO ADD SOME CHECK HERE TO SEE IF THERE'S NO GREATER POSSIBLE SOLUTION GIVEN CURRENTLENGTH, SWITCH OFF SOME GLOBAL FLAG, AND HAVE THAT FLAG BE REQUIRED FOR ALL RECURSIVE CALLS (PROBABLY IN THE FOR LOOP ABOVE WITH SUBWORDS)

    #This section of code starts from the biggest word bucket and works its way down, stopping early if there is no way to get a bigger solution than the one already recorded; this lack of a possible greater solution is indicated by doneFlag = True
    currentLength = maxLength
    doneFlag = False
    while currentLength > 0 and doneFlag == False:
        if currentLength in lengthMap:
            for currentWord in lengthMap[currentLength]:
                #Since we're working from longest to shortest, if the length of the current word - the minimum word + 1 is less than or equal to the solution, then we know it's impossible to get a word bigger than the current solution by iterating through the rest of the words
                if (len(currentWord) - minLength + 1) <= solution:
                    doneFlag = True
                    break
                stringHelper(currentWord)
        currentLength -= 1
    return solution

sampleWordList = {"a", "b", "ba", "bca", "bda", "bdca"}
sampleWordList = {"c", "aa", "baa", "bda", "bdaa"}
print(stringChain(sampleWordList))
