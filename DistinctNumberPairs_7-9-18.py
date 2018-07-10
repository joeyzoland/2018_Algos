"""
Note: This is a mock interview question where you are given a list of integers, and you have to determine the unique number of combinations that add up to a given target, which is an integer.

PseudoCode

Input :[Int]
Target Sum : Int

Output: Int

[1, 2, 3, 6, 7, 8, 9, 1]
10

Output: 3 (1+9, 2+8, 3+7)

Time: O(N)


{1, 2, 3, 6, 7, 8, 9}
             ^

{1, 9, 2, 8, 3, 7}
3


Result initialized to 0; it's going to be the output
Create a visited set
Iterate through the input array, adding contents to a set
Iterate through the set, checking if the complement to reach the target exists
  If it does, check if either the current number or the complement are in the visited set
    If they are not in the visited set, add them and increment result
Return result


"""

def distinctPairs(numberList, target):
  result = 0
  visited = set()
  numberSet = set()
  for number in numberList:
    numberSet.add(number)
  for number in numberSet:
    if (target - number in numberSet and number not in visited):
      visited.add(number)
      visited.add(target - number)
      result += 1
  return result

numberList = [1, 2, 3, 6, 7, 8, 9, 1, -5, 15]
target = 10
print(distinctPairs(numberList, target))

"""
Diagramming

numberSet: {1, 2, 3, 6, 7, 8, 9}
                           ^
          10 - 8 = 2


visited: {1, 9, 2, 8, 3, 7}
result: 3
target: 10
"""
