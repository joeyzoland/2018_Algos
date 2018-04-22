#https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    radiationCount = 0
    for i in range(0, len(s) / 3):
        if (s[i * 3] != "S"):
            radiationCount += 1
        if (s[i * 3 + 1] != "O"):
            radiationCount += 1
        if (s[i * 3 + 2] != "S"):
            radiationCount += 1
    return radiationCount

print(marsExploration("SOS"))
print(marsExploration("BOA"))
