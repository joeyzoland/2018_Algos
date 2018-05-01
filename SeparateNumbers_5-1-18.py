#https://www.hackerrank.com/challenges/separate-the-numbers/problem

#For one digit, check if next index or the next two indices are one greater
#If it is, save the index position of the next number and keep going (if you reach the end, return "Yes" and the first digit to show it was a positive)
#If it was not, add on another index to make a two-digit number out of the beginning of the string, and then check to see if the next two indices or the next three indices after that are one greater; do this until the number of indices at the beginning of the string is equal to half the total length of the string (the next number can't be consecutive if it has less digits than the previous one, which means there can't be any matches left)
#If you don't find any matches, return "No"

import math

def separateNumbers(s):
    if (len(s) == 1):
        print ("NO")
        return
    initialLength = 1
    currentPosition = 0
    currentLength = 1
    secondPosition = 1

    while (math.floor(currentLength <= len(s) / 2)):
        #If either position has a leading zero, you want to reset back to the first position and check if it works with one more digit
        if (len(s) - currentPosition < currentLength or s[currentPosition] == "0" or s[secondPosition] == "0"):
            initialLength += 1
            currentPosition = 0
            currentLength = initialLength
            secondPosition = currentPosition + initialLength
        #Check if the next equal number of digits (next) or number of digits + 1 (bigger) is one greater than the previous; if it is, update so that whatever was in the second position becomes first, and move second position forward; if secondPosition is at the end of the string, you know you got through the whole thing and it is a positive result
        else:
            first = s[currentPosition : currentPosition + currentLength]
            next = s[secondPosition : secondPosition + currentLength]
            bigger = s[secondPosition : secondPosition + currentLength + 1]
            if (int(next) - int(first) == 1):
                currentPosition = secondPosition
                secondPosition += currentLength
                if (secondPosition == len(s)):
                    print ("YES " + s[0:initialLength])
                    return
            elif (int(bigger) - int(first) == 1):
                currentPosition = secondPosition
                currentLength += 1
                secondPosition += currentLength
                if (secondPosition == len(s)):
                    print ("YES " + s[0:initialLength])
                    return
            #If the following digit or two digits are not greater than the first, then you want to reset and try again with one additional digit
            else:
                initialLength += 1
                currentPosition = 0
                currentLength = initialLength
                secondPosition = currentPosition + initialLength
    print ("NO")
    return

#910



print (separateNumbers("8990"))
