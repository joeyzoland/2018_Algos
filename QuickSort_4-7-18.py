#Note: This exercise is a QuickSort; it is not attached to any Hackerrank algorithm and is simply for personal enrichment

import random

def QuickSort(arr, leftBound=0, rightBound=None):
    if (rightBound == None):
        rightBound = len(arr) - 1
    #Checks if there is any space, i.e. any unsorted numbers, that need to be sorted; in recursive calls, if there are no numbers left to be sorted on one side of the divide-and-conquer algorithm, the recursive call should stop
    if (rightBound - leftBound <= 0):
        return
    else:
        pivotPosition = random.randint(leftBound, rightBound)
        pivotValue = arr[pivotPosition]
        #This places the pivot at the beginning of the array/subarray being sorted by the recursive call
        if (pivotPosition != leftBound):
            arr[pivotPosition], arr[leftBound] = arr[leftBound], arr[pivotPosition]
        #sortedIndex keeps track of what is lower than the pivot; if nothing is lower than the pivot in the array/subarray, than sortedIndex simply stays at the pivot position and you know that the pivot is sorted
        sortedIndex = leftBound
        #If something is less than the pivot, than you increment the sortedIndex by 1 to indicate that you have sorted another number correctly, and you move the number to the rightmost position of the sorted numbers and swap whatever was there; note, this starts at leftBound + 1 because the pivot stays in the leftmost position until the end of the recursive call, in which case it is swapped to the rightmost position in the swapped numbers because you know everything to the left is less than it
        for i in range(leftBound + 1, rightBound + 1):
            if (arr[i] < pivotValue):
                sortedIndex += 1
                #Note: If the first number in the array/subarray is also less than the pivot, than it does not need to be swapped because it is already in place
                if (sortedIndex != i):
                    arr[sortedIndex], arr[i] = arr[i], arr[sortedIndex]
        arr[leftBound], arr[sortedIndex] = arr[sortedIndex], arr[leftBound]
        #You run it again on everything to the left of the pivot and everything to the right of the pivot
        QuickSort(arr, leftBound, sortedIndex - 1)
        QuickSort(arr, sortedIndex + 1, rightBound)



sampleArray = [1, 2, 7, 9, 4, 6, 3]
QuickSort(sampleArray)
print(sampleArray)
