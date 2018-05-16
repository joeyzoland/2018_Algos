#https://www.hackerrank.com/challenges/richie-rich/problem

#001240 (4 changes allowed)
#---
#042240 (2 changes required at minimum)
#044440 (3 changes used)
#442244 (4 changes used, optimal)

#Note for the above problem: If you have a one-change and a two-change move that both get you the same amount of increase (e.g., above, changing the central 22 from basline to 44 nets you a 4 point increase, whereas changing each of the outer 0's also gives you a 4 point increase for each), choose the double-move pair instead of the single to get the optimal, as shown above (assuming you have two changes available still)

#Clarification on the above: If you have two or more points left, when trying to determine if your next move should be changes for two separate pairs of changing both sides of one pair, compare the top two one-character changes across two pairs and the maximum change you can get for changing one pair, and go with whatever is highest

#Note to self: Have to find a way to make sure that you are not left with one change at the end that cannot be used!!!  If you have an odd number of changes left after hitting the base case, maybe start off by taking the highest one point move that you can at first, then go from there by looking at pairs with your even number of changes remaining?



#000091 (4 changes)
#---
#190091 (2 changes required at minimum)
#199991 (4 changes used, optimal)

#00000912 (5 changes)
#---
#21900912 (3 changes required at minimum)
#^^^
#21999912 (5 changes used)
#^^^^^
#99900999 (5 changes used, optimal)
#^^^   ^^

#00077912 (5 changes)
#---
#21977912 (3 changes required at minimum)
#^^^
#21999912 (5 changes used)
#^^^^^
#99977999 (5 changes used, optimal)
#^^^   ^^



#Same number of changes as minimum required, go with minimum
#One more try than required number of changes, change the lowest changed pair to be a pair of maximums
#Two or more tries than required

import math
def highestValuePalindrome(s, n, k):
    counter = 0
    solution = s
    #ChangeSet is a set of indices indicating where a pair was changed
    changeSet = set()
    # maximumIndex = 0
    for index in range(0, int(math.floor(n / 2))):
        first = index
        last = len(s) - 1 - index

        #AT first, I thought you could only change characters of the string to the character in the string with the highest value, but this doesn't seem to be true anymore...

        # #We initialize maximum to the first value; I realize we are comparing the first value to itself twice if the first and last characters don't match, but it's not a big deal
        # if s[first] > s[maximumIndex] or s[last] > s[maximumIndex]):
        #     if (s[first] == s[last] or s[first] > s[last]):
        #         maximumIndex = first
        #     else:
        #         maximumIndex = last

        #If the two characters in a pair differ, we change the lower value to the higher value, and include the pair's position in changeSet
        if (s[first] != s[last]):
            if (s[first] > s[last]):
                greatest = first
                least = last
            else:
                greatest = last
                least = first
            #Concatenating solution string to change the lower value to the highest value
            solution = solution[0:least] + solution[greatest] + solution[least + 1:]
            changeSet.add(index)
            counter += 1
    if (k < counter):
        return -1
    else:
        if (counter % 2 == 1):
            #If no changes were made, you might as well just ignore the 1 remainder of change pairs, because you will never be able to use it
            if (len(changeSet) == 0):
                counter -= 1
            firstIteration = True
            else:
                for changeIndex in changeSet:
                    if (firstIteration == True):
                        minimumIndex = changeIndex
                        firstIteration = False
                    else:
                        if (solution[changeIndex] < solution[minimumIndex]):
                            minimumIndex = changeIndex
                #Now, you have found the changed pair with the lowest value, so you can switch them both to the maximum value to get the greatest gain

                #Note: If the middle number is lower than the maximum, you may want to increase that to get the maximum increase



print(highestValuePalindrome("0010", 4, 1))
