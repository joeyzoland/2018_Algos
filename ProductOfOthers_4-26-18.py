#Note: This algorithm was taken from an online source besides HackerRank.  You are given an array of numbers, and you have to return another array of numbers that is the product of all other numbers except for the one that you are currently on.  For example, [1, 2, 3] returns [2 * 3, 1 * 3, 1 * 2] => [6, 3, 2]

def get_products_of_all_ints_except_at_index(inputList):
    solutionsArray = inputList[:]
    pastProduct = 1
    #First, we iterate through the entire list so that the solutionsArray is holding the product of everything that came before it.
    for i in range(0, len(solutionsArray)):
        solutionsArray[i] = pastProduct
        pastProduct *= inputList[i]
    pastProduct = 1
    #Secondly, we run through it one more time from back to front, multiplying the current value in solutionsArray by what came after it.
    for i in range(len(solutionsArray) - 1, -1, -1):
        solutionsArray[i] *= pastProduct
        pastProduct *= inputList[i]
    print (solutionsArray)

get_products_of_all_ints_except_at_index([1, 7, 3, 4])
