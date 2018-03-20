#https://www.hackerrank.com/challenges/arrays-ds/problem

#reverseArray takes in an array and returns a string with all of the characters in reverse order, separated by spaces

def reverseArray(arr):
    result = "";
    for x in range (len(arr) - 1, -1, -1):
        result += str(arr[x]) + " "

    #Removes the final space from the string
    result = result[:-1]

    print (result)

arr = [0, 3, 4]
reverseArray(arr)
