#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

# This first function was me checking if the letters in comparison were in the input string in any order; the one below matches the problem, which checks if the letters in "s" match comparison in the same order as comparison

# def hackerrankInString(s):
#     comparison = "hackerrank"
#     frequencyHolder = {}
#     comparisonHolder = {}
#     for char in comparison:
#         if (char not in comparisonHolder):
#             frequencyHolder[char] = 0
#             comparisonHolder[char] = 1
#         else:
#             comparisonHolder[char] += 1
#     #After the above code, frequencyHolder is initilialized to keep track of the frequencies of relevant variables in the "s" string, whereas comparisonHolder holds the desired minimum frequency of each letter in comparison; please note that you can simply change the "comparison" variable and this function will check if that word is present in s as well
#     #frequencyHolder = {"h":0, "a":0, "c":0, "k":0, "e":0, "r":0, "n":0}
#     #comparisonHolder = {"h":1, "a":2, "c":1, "k":2, "e":1, "r":2, "n":1}
#
#     #The below code updates frequencyHolder with relevant character frequencies until the frequencies in comparisonHolder are matched; at the end, if the two dictionaries match, you know the word was contained in "s"
#     for character in s:
#         if (character in frequencyHolder):
#             if (frequencyHolder[character] < comparisonHolder[character]):
#                 frequencyHolder[character] += 1
#     print (comparisonHolder)
#     print (frequencyHolder)
#     if (comparisonHolder == frequencyHolder):
#         return "YES"
#     return "NO"

def hackerrankInString(s):
    comparison = "hackerrank"
    comparisonIndex = 0
    #This function simply tracks when each character in comparison is hit in the string "s," and if we reach the last index of comparison, we know that comparison was in "s" so we return YES; otherwise, we return No
    for character in s:
        if (character == comparison[comparisonIndex]):
            comparisonIndex += 1
        if (comparisonIndex == len(comparison)):
            return "YES"
    return "NO"

print(hackerrankInString("rankhackerer"))
print(hackerrankInString("ilovehackersandiloveranks"))
