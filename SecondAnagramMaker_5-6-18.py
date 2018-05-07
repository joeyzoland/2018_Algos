#https://www.hackerrank.com/challenges/making-anagrams/problem

#Make an object for each string with a character as the key and its frequency as the value
#Iterate through the first string object:
    #If the character isn't in the second string, add its frequency to the change variable
    #Else if the character is in the second string, add the absolute value of the difference between the two frequencies to the change variable, then pop that key from the second dictionary
#Iterate through the remainder of the second string object:
    #For every remaining key that was not existant in the first object (i.e., that was not popped), add it's frequency to the change variable
#Return the change variable

def makingAnagrams(s1, s2):
    firstObject = {}
    secondObject = {}
    change = 0

    for character in s1:
        if (character not in firstObject.keys()):
            firstObject[character] = 1
        else:
            firstObject[character] += 1
    for character in s2:
        if (character not in secondObject.keys()):
            secondObject[character] = 1
        else:
            secondObject[character] += 1

    for key in firstObject:
        if (key not in secondObject):
            change += firstObject[key]
        else:
            change += abs(firstObject[key] - secondObject[key])
            del secondObject[key]
    for key in secondObject:
        change += secondObject[key]

    return change

sampleString1 = "cde"
sampleString2 = "abc"
print (makingAnagrams(sampleString1, sampleString2))
