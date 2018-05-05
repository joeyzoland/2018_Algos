#https://www.hackerrank.com/challenges/anagram/problem

#This function takes in a string as input, splits it into two equal halves, and outputs the number of character changes that are necessary to make one half an anagram of the other

def anagram(s):
    if (len(s) % 2 == 1):
        return -1
    firstString = s[0: len(s) / 2]
    secondString = s[len(s) / 2:]
    firstObject = {}
    secondObject = {}
    changes = 0

    #This makes an object out of the first and second halves of the string, with the character as the key and the character's frequency as its value
    for index in range(0, len(firstString)):
        if (firstString[index] not in firstObject.keys()):
            firstObject[firstString[index]] = 1
        else:
            firstObject[firstString[index]] += 1
        if (secondString[index] not in secondObject.keys()):
            secondObject[secondString[index]] = 1
        else:
            secondObject[secondString[index]] += 1

    #This iterates through the firstObject and sees which values differ from the second object, and adds the number of differences to "change"
    for key in firstObject:
        if key not in secondObject.keys():
            changes += firstObject[key]
        elif (firstObject[key] > secondObject[key]):
            changes += firstObject[key] - secondObject[key]

    return changes

sampleArray = ["aaabbb",
"ab",
"abc",
"mnop",
"xyyx",
"xaxbbbxx"]

for i in sampleArray:
    print (anagram(i))
