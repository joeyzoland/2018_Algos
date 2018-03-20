#https://www.hackerrank.com/challenges/crush/problem

#Original, brute-forced solution.  Creates a new "array" that tracks the actual value of each position.  For instance, an array with [6, 3] has a first position with an absolute height of 6 and a second position with am absolute height of 3.

def ArrayManipulation(arraySize, arrayOperations):
    array = []
    for _ in range(0, arraySize):
        array.append(0)
    for i in range(len(arrayOperations)):
        a, b, k = [int(n) for n in arrayOperations[i]]
        for j in range(a - 1, b):
            array[j] += k
    max = array[0]
    for x in range(1, len(array)):
        if (array[x] > max):
            max = array[x]
    print (max)

#Refined solution, adapted after reviewing HackerRank discussion boards.  Creates a new "array" that tracks the values of changes.  In essence, you're creating an array that depicts the hills and valleys of changes, with each value's height being calculated relative to the position of the value's height preceding it.  Rather than n^2 complexity like the first solution, this one is linear because you only have to change two values on each iteration of arrayOperations.  See below for more information about this refinement:

def ArrayManipulation2(arraySize, arrayOperations):
    array = []
    for _ in range(0, arraySize):
        array.append(0)
    for i in range(len(arrayOperations)):
        a, b, k = [int(n) for n in arrayOperations[i]]
        #You add on k to symbolize the mountain climbing upwards at the "a" value.  If there is a value before it, the second value is taller by k units.
        array[a - 1] += k
        #You use -k to symbolize that the hill is dropping off into a valley after the "b" value; it has a negative relative height compared to the value before it.
        if ((b + 1) <= len(array)):
            array[b] -= k
    #The first value in the array matches the solution above and is the exact height.  However, everything afterwards is calculated by looking at the value preceding it.  The variable "current" combines the past height and the next height to produce the actual height of the current value.  For instance, an array with [3, -3] has absolute heights of [3, 0], because the first position is 3 and the second position is -3 relative to the first position's absolute height of 3, so the second position has an absolute height of 0 (3 - 3).
    max = array[0]
    current = array[0]
    for x in range(1, len(array)):
        current += array[x]
        if (current > max):
            max = current
    print (max)

ArrayManipulation2(5, [[1, 2, 2], [2, 4, 5]])
