#https://www.hackerrank.com/challenges/funny-string/problem

#First, we divide the string into first and second halves (note that if the length of the string is odd, they will share that same letter).  Then, we iterate through, using ord to give us a unique value for each letter and to track distance (a = 1, b = 2, etc.).  If the absolute difference between each corresponding pair is not the same, we return "Not Funny" to signify a negative result.  If they are the same, we keep iterating through the list until we have examined the entire string, in which case we return "Funny" to signify a positive result.

import math

def funnyString(s):
    firstHalf = s[0 : int(math.ceil(len(s) / 2))]
    secondHalf = s[int(math.floor(len(s) / 2)) : ]
    for i in range(0, len(firstHalf)):
        first1 = ord(s[i]) - 96
        first2 = ord(s[i + 1]) - 96
        second1 = ord(s[-(i + 1)]) - 96
        second2 = ord(s[-(i + 2)]) - 96
        if (abs(first1 - first2) != abs(second1 - second2)):
            return ("Not Funny")
    return ("Funny")

sampleArray = ["jkotzxzxrxtzytlruwrxytyzsuzytwyzxuzytryzuzysxvsmupouysywywqlhg", "eklrywzvpxtvoptlrskmskszvwzsuzxrtvyzwruqvyxusqwupnurqmtltnltsmuyxqoksyurpwqpv",
"efhpuvqvnuwpvwysvnunostvpqvxtxsvqwqvsxtxvqpvtsonunvsywvpwunvqvupxzy",
"otytmpszumnryqvxpvnvxyvpvprumnvsqwqwtsqyqksqvnuqpxszwzsxsx",
"bhmptlqswsvoqsvzyzwoqtvowpyqxpwurpxutswtrpwzvrpkswzuo",
"rvovprxzvwrxpwpzsltzutxztrxqxt",
"ceiosyrtztvnqsuozrxvtqywqwyrxtnjh",
"djnsyzxszryqworuxpqvqwquvotzsqvoupwvztzupowtqnvpxqyrwutzuys",
"kovzuywsuvwxuxtwzryzuxyvouvyskoqtwryszxqqxzsyrwtqoksyvuovyxuzyrzwtxuxwvuswuqvryu",
"ptvzstvotxqyvzrwyqryzrpkswzryupwutmigc"]
for i in sampleArray:
    print(funnyString(i))
