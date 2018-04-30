#https://www.hackerrank.com/challenges/gem-stones/problem

#PSEUDOCODE
#Iterate through each element of the first array
#Check if each element is in each of the other arrays: If it is not, break and iterate through the next element.  If it is, continue to the next array.  If you iterate through all arrays and that element is not in your solutions set, add that element to your solutions set and increase the count.
#Return the count.

def gemstones(arr):
    solutionsSet = set()
    count = 0
    for x in arr[0]:
        flag = True
        for y in range(1, len(arr)):
            if (x not in arr[y]):
                flag = False
                break
        if (flag == True):
            if (x not in solutionsSet):
                solutionsSet.add(x)
                count += 1
    return count
