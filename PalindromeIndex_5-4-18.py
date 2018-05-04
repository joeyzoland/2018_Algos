#https://www.hackerrank.com/challenges/palindrome-index/problem

# First draft of pseudocode
#First, check if the string is already a palindrome; if it is, return -1
#If the string isn't a palindrome, remove a letter and check if it's a palindrome again; if it is, return the index of the character you removed; if it's not, try the other letter

#This keeps track of the first palindrome check with the parameter inner = false; if the check of the entire string for a palindrome matches, then we return -1. Otherwise, where the mismatch occurs, we run the function on two substrings (each removing one of the two mismatched characters) to see if either becomes a palindrome.  If it does, we return the character we removed, otherwise, we set nonPalindrome to False and keep going.  If we don't find any more mismatches and nonPalindrome = True, we return an error message saying it can't become a palindrome.
def palindromeIndex(s, inner = False):
    midpoint = int(math.floor(len(s) / 2))
    if (inner == False):
        nonPalindrome = False
    for index in range(0, midpoint):
        first = s[index]
        last = s[(index * -1) - 1]
        if (first != last):
            if (inner == False):
                newString1 = s[0:index] + s[index + 1:]
                newString2 = s[0:len(s) - index - 1] + s[len(s) - index:]
                if (palindromeIndex(newString1, True) == -1):
                    return index
                elif (palindromeIndex(newString2, True) == -1):
                    return len(s) - index - 1
                else:
                    nonPalindrome = True
            else:
                return
    if (inner == False):
        if (nonPalindrome == True):
            return ("This cannot become a palindrome with one character removal")
    return -1

print(palindromeIndex("abcbe"))



# Archived Brute-forced code
#This code looks through a string until it finds a mismatch that stops that string from being a palindrome; then, it removes each character being compared, and checks each of those substrings to see if either of them is a palindrome; if it is, it returns the index of the removed character, otherwise, it goes back to the first loop described and repeats the process
# def palindromeIndex(s):
#     midpoint = int(math.floor(len(s) / 2))
#     for index in range(0, midpoint):
#         first = s[index]
#         last = s[(index * -1) - 1]
#         if (first != last):
#             flag = True
#             newString = s[0:index] + s[index + 1:]
#             newMidpoint = int(math.floor(len(newString) / 2))
#             for newIndex in range(0, newMidpoint):
#                 newFirst = newString[newIndex]
#                 newLast = newString[(newIndex * -1) - 1]
#                 if (newFirst != newLast):
#                     flag = False
#                     break;
#             if (flag == True):
#                 return index
#             else:
#                 flag = True
#                 newString = s[0:len(s) - index - 1] + s[len(s) - index:]
#                 newMidpoint = int(math.floor(len(newString) / 2))
#                 for newIndex in range(0, newMidpoint):
#                     newFirst = newString[newIndex]
#                     newLast = newString[(newIndex * -1) - 1]
#                     if (newFirst != newLast):
#                         flag = False
#                         break;
#                 if (flag == True):
#                     return len(s) - index - 1
#     return -1
