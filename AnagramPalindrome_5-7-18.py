#https://www.hackerrank.com/challenges/game-of-thrones/problem

#Sort the input
#Iterate through the input, checking if the next character matches your current one;
    #If it does
        #Increment your frequency variable
    #If it does not
        #If the frequency is odd
            #If there has not yet been an odd frequency, record that there has now been one
            #If there has, break the function and return false
        #Else if the frequency is even
            #Continue
        #In both cases, reset the frequency variable
#If you reach the end of the input, check the frequency and run the same above conditions
#If you reach the very end, return true

def gameOfThrones(s):
    if (len(s) == 0):
        return "NO"
    sortedString = "".join(sorted(s))
    #OddFlag keeps track of whether there has already been an odd frequency; if there is more than one odd frequency, it is impossible for it to be an anagram of a palindrome because there can only be one odd frequency in the center, so we return aFalse
    oddFlag = False
    currentChar = sortedString[0]
    frequency = 1
    for index in range(1, len(sortedString)):
        if (sortedString[index] == currentChar):
            frequency += 1
        else:
            if (frequency % 2 == 1):
                if (oddFlag == False):
                    oddFlag = True
                else:
                    return "NO"
            frequency = 1
            currentChar = sortedString[index]
    #This last line makes sure that the string doesn't fail the check on the last frequency (the check above doesn't happen for the last frequency because the "for" loop ends before that)
    if (frequency % 2 == 1 and oddFlag == True):
        return "NO"
    return "YES"


sampleInput = "cdcdcdcdeeeef"
print(gameOfThrones(sampleInput))
