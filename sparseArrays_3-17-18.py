#https://www.hackerrank.com/challenges/sparse-arrays/problem

def sparseArrays(strings, queries):
    for i in range (0, len(queries)):
        count = 0
        for j in range (0, len(strings)):
            if (queries[i] == strings[j]):
                count += 1
        print (count)

sampleStrings = ['aba', 'baba', 'aba', 'xzxb']
sampleQueries = ['aba', 'xzxb', 'ab']
sparseArrays(sampleStrings, sampleQueries)
