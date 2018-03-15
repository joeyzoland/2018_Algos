#This function takes in an array (6 X 6 in the example) and finds the greatest sum of numbers within an hourglass structure within that array

def hourglassArray(arr):
    for y in range(0, len(arr) - 2):
        for x in range(0, len(arr) - 2):
            hourglassSum = 0
            hourglassSum += arr[y][x]
            hourglassSum += arr[y][x + 1]
            hourglassSum += arr[y][x + 2]
            hourglassSum += arr[y + 1][x + 1]
            hourglassSum += arr[y + 2][x]
            hourglassSum += arr[y + 2][x + 1]
            hourglassSum += arr[y + 2][x + 2]
            if (y == 0 and x == 0):
                result = hourglassSum
            elif (hourglassSum > result):
                result = hourglassSum
    return result


sampleArray = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 0, 2, 2, 2],
[0, 0, 0, 0, 2, 0],
[0, 0, 0, 2, 2, 0]]

print(hourglassArray(sampleArray))
