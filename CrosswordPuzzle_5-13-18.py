#https://www.hackerrank.com/challenges/crossword-puzzle/problem

#Iterate through crossword with an xPosition and a yPosition until you find a "-" sign
#When you find a minus sign, check if there are any characters above and, if there are, check if you have a word that can fit those characters and any "-'s" that are below it; if that isn't true, check if there are any characters to the left and, if there are, for every word that does fit, plug it in and make a recursive call; finally, if there are no characters above or left, check if there are minuses below and to the right, and repeat the usual process
#If at any point no word can fit, return nothing
#If you reach the end of crossword, return the completed crossword



#Note to self: Will probably have to transform crossword into an array, unless you want to make the changing of the crossword syntax concatenate strings around the character you are changing, rather than only modifying the character itself (since strings are immutable and arrays are not)

import copy

def crosswordPuzzle(crossword, hintDict, yPosition = 0, xPosition = 0):
    #Transforms the hints, which are given to you as a string, into an object with the length of each word as the key, and the value as a set of all words of that length
    if (isinstance(hintDict, basestring)):
        hints = hintDict
        hintDict = {}
        for hint in hints:
            if (len(hint) not in hintDict.keys()):
                hintDict[len(hint)] = set(hint)
            else:
                hintDict[len(hint)].add(hint)

    xLength = len(crossword[0])
    yLength = len(crossword)

    #While you have not iterated through the entire crossword
    while(xPosition != xLength and yPosition != yLength):
        #If the character you are on is a "-"
        if(crossword[y][x] == "-"):
            #If you are in the top row, meaning there's no need to check if there are any letters in the spaces above you
            if(yPosition == 0):
                #If the character below you is also empty, which means you'll have to insert a word
                if(crossword[y - 1][x] == "-"):
                    #These below lines are used to simply count the amount of empty spaces we have, so we can pick a word from our hintDict that matches that length
                    counter = yPosition + 1
                    while(crossword[counter][x] == "-"):
                        if (counter + 1 == yLength):
                            counter += 1
                            break
                        counter += 1
                    distance = counter - yPosition
                    #If we have a word of the designated length in our hintDict, then we need to plug it in and run a recursive call to continue running our function
                    if (distance in hintDict.keys()):
                        for possibility in hintDict[distance]:
                            newCounter = 0
                            crosswordCopy = crossword
                            while (newCounter < distance):
                                crosswordCopy[newCounter + yPosition][xPosition] = possibility[newCounter]
                                newCounter += 1
                            hintDictCopy = copy.deepcopy(hintDict) hintDictCopy[distance].remove(possibility)
                            #Make sure this operation is actually happening in hintDictCopy, rather than a copy of the set that is not connected to hintDictCopy (I believe it should be as this is passed by reference, but might be a good place to troubleshoot if things go south)

                            solution = crosswordPuzzle(crosswordCopy, hintsCopy, yPosition, xPosition, hintDictCopy)

                            #We'll have crosswordPuzzle return a crossword only if it successfully finishes all of the loops; otherwise, we'll have it return false, and this will continue

                            if (solution == False):
                                continue
                            else:
                                return solution
                                
