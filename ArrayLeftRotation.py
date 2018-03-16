def leftRotationArray(arr, rotations):
    for h in range (0, rotations):
        for i in range (0, len(arr) - 1):
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
        print (arr)
    result = ""
    for j in range (0, len(arr)):
        result += str(arr[j])
        if (j < len(arr) - 1):
            result += " "
    return result

sampleArray = [1, 2, 3, 4, 5]
print(leftRotationArray(sampleArray, 4))
