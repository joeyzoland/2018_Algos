#https://www.hackerrank.com/challenges/array-left-rotation/problem

def leftRotationArray(arr, rotations):
    resultArray = []
    result = ""
    for h in range (0, len(arr)):
        trueRotations = (rotations + h) % len(arr)
        resultArray.append(arr[trueRotations])
    for j in range (0, len(arr)):
        result += str(resultArray[j])
        if (j < len(resultArray) - 1):
            result += " "
    return result

sampleArray = [1, 2, 3, 4, 5]
print(leftRotationArray(sampleArray, 5))
