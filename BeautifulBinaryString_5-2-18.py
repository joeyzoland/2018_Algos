#https://www.hackerrank.com/challenges/beautiful-binary-string/problem

#First Draft of Pseudocode
#Iterate through the string, if the number is 0...
    #If the numbers recorded in the two tracking variables are 0 and 1, move onto the next character and increment the count by 1 (a change is necessary)
    #Otherwise, record this 0 in one of the two tracking variables
#If the number is 1...
    #Check if the number preceding was a 0; if so, record these and move on
    #If the last number was a 1, you can simply skip to the next character
#Return the count

def beautifulBinaryString(b):
    if (len(b) < 2):
        return 0
    first = False
    second = False
    count = 0
    iterationCounter = 0
    for character in b:
        iterationCounter += 1
        if (character == "0"):
            #If both first and second matched, then you can leave increment the count and change the last 0 to a 1, thus setting first to be false because it is now a 1.  Otherwise, the 0 can stay as it is, and it might be the start of a new beautiful string
            if (first and second):
                count += 1
                first = False
            else:
                first = True
            #Regardless of whether there was a match, this should be reset (in case of match, it doesn't work anymore because the last "0" is now a 1; in case of a non-match, it means there wasn't a 0-1 setup previously, so you have to start over from here with this being the first 0)
            second = False

            #If the first character matched (was a 0), but the second character match of 1 was not made yet, then this is the "1" and second can be set to True!  Otherwise, the potential beautiful string ends here, and both the first and second have to be reset to False
        elif (character == "1"):
            # print ("check2")
            if (first and not second):
                second = True
            else:
                first = False
                second = False
    return count

sample = "01101"
print beautifulBinaryString(sample)
