#https://www.hackerrank.com/challenges/alternating-characters/problem

#Record the first character of the string in a variable
#Iterate through the rest of the string; if the next character differs from what was before, simply update the variable recording the last letter; if the next character is the same, simply update the count
#Return the count

def alternatingCharacters(s):
    lastLetter = s[0]
    count = 0
    for i in range (1, len(s)):
        if (s[i] != lastLetter):
            lastLetter = s[i]
        else:
            count += 1
    return count



sampleInputsArray = ['AAAA',
'BBBBB',
'ABABABAB',
'BABABA',
'AAABBB']

for input in sampleInputsArray:
    print(alternatingCharacters(input))
