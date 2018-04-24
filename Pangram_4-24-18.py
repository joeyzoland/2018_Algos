#https://www.hackerrank.com/challenges/pangrams/problem

#This function iterates through every letter of the alphabet to see if there is a match at any letter of the input string; if it at any point the string is found to be missing a letter, the function returns a negative result because it cannot be a pangram.  If it iterates through the entire alphabet and finds a match for each letter, it returns a positive result.

def pangrams(s):
    lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    for lowercaseLetter in lowercaseAlphabet:
        letterMatch = False
        for character in s:
            if (character.lower() == lowercaseLetter):
                letterMatch = True
                break
        if (letterMatch == False):
            return "not pangram"
    return "pangram"

#Sample1 with entire alphabet = pangram
sample1 = "We promptly judged antique ivory buckles for the next prize"
#Sample2 missing x = not pangram
sample2 = "We promptly judged antique ivory buckles for the prize"

print pangrams(sample1)
print pangrams(sample2)
