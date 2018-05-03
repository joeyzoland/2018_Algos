#https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

#Iterates through the word, starting from the front and ending at the midpoint
#Tracks the difference between the character in the first half of the word and the second half of the word, using ord (ord(a) = 97 and ord(b) = 98, so the absolute difference between them is 1)
#Increments count with each difference

import math

def theLoveLetterMystery(s):
    midpoint = int(math.floor(len(s) / 2))
    count = 0
    for index in range(0, midpoint):
        first = s[index]
        last = s[(-1 * index) - 1]
        difference = abs(ord(first) - ord(last))
        count += difference
    return count

sampleArray = ["abc",
"abcba",
"abcd",
"cba"]

for sample in sampleArray:
    print(theLoveLetterMystery(sample))
