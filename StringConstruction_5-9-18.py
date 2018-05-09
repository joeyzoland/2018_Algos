#https://www.hackerrank.com/challenges/string-construction/problem

#If you really think about this problem, all you need to do is count the number of unique characters in the string and return it

#Pseudocode
#Initialize a set and counter variable, and then iterate through the string
#If a character is not in the set:
    #Increment the count variable and append it to the set
#If it is in the set
    #Simply continue to the next iteration
#Return the count

def stringConstruction(s):
    ourSet = set()
    counter = 0
    for char in s:
        if (char not in ourSet):
            counter += 1
            ourSet.add(char)
    return counter

print(stringConstruction("abab"))
