#https://www.hackerrank.com/challenges/the-power-sum/problem

#This function searches vertically and horizontally, subtracting each integer squared by N that is less than the remainder, and then calling itself again to subtract the next greatest against the remainder.  If at any point current comes out to exactly 0, you know you have found a combination of squares that add up to the target, so you add 1 to sum.  After checking each subset of possible squares against the remainder (either having the remainder reach 0 or less than 0 and changing continueFlag to False), the function returns sum, which has counted recursively how many perfect square subsets there were.

def powerSum(X, N, last = 1):
    sum = 0
    counter = last
    continueFlag = True
    while (continueFlag):
        current = X - counter**N
        if(current < 0):
            continueFlag = False
        elif(current == 0):
            sum += 1
            continueFlag = False
        else:
            sum += powerSum(current, N, counter + 1)
        counter += 1
    return sum

print(powerSum(10, 2))

#First draft of code is archived below; did not work as well with a for loop because of multiple type conversions and resulting rounding errors (e.g., the third root of 64 comes out as 3, instead of correctly 4)
# def powerSum(X, N, last = 1):
#     sum = 0
#     # print("outside loop")
#     print ("outer last is", last)
#     print("last", last)
#     print("X", X)
#     for i in range(last, int(round(X ** (1/float(N)))) + 1):
#         print ("inner last is", last)
#         # print("insde loop")
#         # print("i**N", i**N)
#         # print("X", X)
#         # print("last is", last)
#         if (i**N == X):
#             sum += 1
#         current = X - i**N
#         # print ("last is", last)
#         # print ("i is", i)
#         # print ("current is", current)
#         if(current > 0):
#             sum += powerSum(current, N, i + 1)
#     return sum
