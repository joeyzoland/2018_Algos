#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem



#First draft of pseudocode (got changed a bit in implementation, but this was a good starting point)

#Sort the string
#Initialize a character count variable and an object, which will hold same-letter frequencies as the keys and the frequencies of those letters of characters as the values (note: there will only be two key-value pairs, because any more than that means the string cannot be made valid with a one character cut)
#Iterate through from left to right
    #If the character is the same as the one previous, increment the count and keep going
    #Else (if the character is different):
        #If the current count exists in the object as a key
            #If its value is 2:
                #Continue
            #If its value is 1:
                #Iterate through the object's keys
                    #If there are no keys with value 2
                        #Increment the current key to value 2 and continue
                    #Else
                        #Return "NO"
        #Else (if the key doesn't exist):
            #If the length of the dictionary is 2:
                #Return "NO"
            #Else if the length of the dictionary is 1:
                #If the existing key is within one space of the current frequency
                    #Append the key to the dictionary with a value of 1
                #Else:
                    #Return "NO"
            #Else (if the dictionary is empty):
                #Append the key to the dictionary with a value of 1
    #Do one final similar check when you reach the end of the string (similar to the steps above when the character doesn't match the previous)
    #If you make it to the end, return "YES"

#"aaabbcc"
#{2:2, 3:1}



def isValid(s):
    sortedS = "".join(sorted(s))
    freqDict = {}
    count = 1
    currentChar = sortedS[0]
    for index in range(1, len(sortedS)):
        if (sortedS[index] != currentChar):
            if (count in freqDict):
                if (freqDict[count] == 1):
                    for key in freqDict.keys():
                        #Finds the key besides the key that you're working with, if there is one, and checks if that key a.) already has 2 frequencies, in which case there is no valid string because you can't have two 2-frequency keys or b.) the difference between the key you are not touching and the one you are adding to is 1, in which case it could be valid because you can subtract off one from the untouched key because its frequency has to be 1 to pass the aforementioned check, although another exception to this is that the key you are not touching could be 1 and still be valid because you could just subtract it off since you can remove one character
                        if (key != count):
                            if (freqDict[key] == 2 or not (key - count == 1 or key == 1)):
                                return "NO"
                    freqDict[count] = 2
            else:
                if (len(freqDict) == 2):
                    return "NO"
                else:
                    #This is not valid if the key you are not touching is more than one space away from what you are adding, as you can only subtract one unit; the exception to this is that it can still be be valid if the preexisting key has a value of 1 and a frequency of 1 because you could remove it, or the new key you are creating is a 1 because you could remove it (it only has a frequency of 1 upon creation)
                    if(len(freqDict) == 1):
                        if ((abs(freqDict.keys()[0] - count) > 1) and not (freqDict.keys()[0] == 1 and freqDict[freqDict.keys()[0]] == 1) and (count != 1)):
                            return "NO"
                    freqDict[count] = 1
            currentChar = sortedS[index]
            count = 1
        else:
            count += 1

    #Run one last mini-check on what was at the end of the string, just to make sure it doesn't fail at the end
    if (count in freqDict):
        if (freqDict[count] == 1):
            for key in freqDict.keys():
                if (key != count):
                    if (freqDict[key] == 2 or not (key - count == 1 or key == 1)):
                        return "NO"
    else:
        if (len(freqDict) == 2):
            return "NO"
        else:
            if(len(freqDict) == 1):
                if ((abs(freqDict.keys()[0] - count) > 1) and not (freqDict.keys()[0] == 1 and freqDict[freqDict.keys()[0]] == 1) and (count != 1)):
                    return "NO"
    return "YES"

sampleString = "cbbbddd"
print(isValid(sampleString))

#shorthand for freqDict test cases
#(1:1, 3:1^)


#For debugging purposes
# def sortString(s):
#     dict = {}
#     for char in s:
#         if char not in dict.keys():
#             dict[char] = 1
#         else:
#             dict[char] += 1
#     return dict
# print (sortString(sampleString))
