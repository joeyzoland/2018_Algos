#Note: This exercise is a MergeSort; it is not attached to any Hackerrank algorithm and is simply for personal enrichment

import math

def mergeSort(array):
    if (len(array) == 1):
        return array
    #This recursively splits the array into left and right portions as long as there are two or more elements in the array
    elif (len(array) > 1):
        left = mergeSort(array[0:int(math.ceil(len(array) / 2))])
        right = mergeSort(array[int(math.ceil(len(array) / 2)):])
        solution = []
        leftPosition = 0
        rightPosition = 0
        #This loop continues to make comparisons until either the left or right arrays run out of items; it simply checks the current index of both arrays and adds the one with the lower value to the solutions array
        while (leftPosition < len(left) and rightPosition < len(right)):
            if (left[leftPosition] < right[rightPosition]):
                solution.append(left[leftPosition])
                leftPosition += 1
            else:
                solution.append(right[rightPosition])
                rightPosition += 1

        #As one of the two arrays will run out of items before the other, this checks which array still has items to it and concatenates them to the end of the solutions array
        if (leftPosition < len(left)):
            solution += left[leftPosition:]
        elif (rightPosition < len(right)):
            solution += right[rightPosition:]
        return solution

print(mergeSort([3, 4, 2, 1, 5, 0]))
