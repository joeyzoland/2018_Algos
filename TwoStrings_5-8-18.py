#https://www.hackerrank.com/challenges/two-strings/problem

#Brute-Force: Iterate through the first string, iterate through the second string to see if the current first string character matches a character in the second string
    #If it does, return "YES"
    #If it does not, continue iterating through the second string; if you go through the last first string character iteration and there's still no match, return "NO"

# def twoStrings(s1, s2):
#     for char1 in s1:
#         for char2 in s2:
#             if (char1 == char2):
#                 return "YES"
#     return "NO"


#Alternative solution: sort both string1 and string2
#Make a variable to record position in both string1 and string2
#While string1 position variable is not greater than string1 length and string2 position variable is not greater than string2 length
    #If string1 value == string2 value, return "YES"
    #Else
        #If string1 value > string2 value
            #Iterate string2 value\
        #Else
            #Iterate string1 value
#If the loop ends, return "NO"

def twoStrings(s1, s2):
    string1Index = 0
    string2Index = 0
    sortedS1 = "".join(sorted(s1))
    sortedS2 = "".join(sorted(s2))
    while (string1Index < len(sortedS1) and string2Index < len(sortedS2)):
        string1Value = sortedS1[string1Index]
        string2Value = sortedS2[string2Index]
        if (string1Value == string2Value):
            return "YES"
        #This code checks for duplicates by saying, "We're looking at the lowest character in string1 and the lowestcharacter in string2.  If string1's value is less than string2's value, then string1's match for string2 must be further up string1."  Same goes for the opposite scenario.  You just keep doing this until you've iterated all of the way through one of the strings in O(N) complexity.
        else:
            if (string1Value < string2Value):
                string1Index += 1
            else:
                string2Index += 1
    return "NO"

firstSampleString1 = "aced"
firstSampleString2 = "dgb"
print twoStrings(firstSampleString1, firstSampleString2)
