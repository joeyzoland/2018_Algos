#https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    if (len(s) == 0):
        return 0
    elif (len(s) == 1):
        return 1
    count = 1
    for character in s[1:]:
        if (character.isupper() == True):
            count += 1
    return count

print(camelcase("chickenOfTheSea"))
