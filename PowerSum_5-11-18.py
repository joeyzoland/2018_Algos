#https://www.hackerrank.com/challenges/the-power-sum/problem

def powerSum(X, N, last = 1):
    sum = 0
    print("ran for loop")
    for i in range(last, int(X ** (1/float(N))) + 1):
        if (i**N == X):
            sum += 1
        current = X - i**N
        print ("last is", last)
        print ("i is", i)
        print ("current is", current)
        sum += powerSum(current, N, i + 1)
    return sum

print(powerSum(100, 3))
