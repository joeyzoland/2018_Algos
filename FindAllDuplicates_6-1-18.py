#leetcode
#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

#NOTE: They ask if you can do this problem with O(N) runtime, and I think you could get near that if you sorted the array in place, and simply deleted every entry that had a match from the array and returned the original array, but that sounds innefficient so I'm going to do it with a hash map

#NOTE: You could also add each of the nums to a set if it isn't present in the set, then append a number to the solutions array if it is already in the set, but I did it the way I did because it can handle there being more than two instances of a duplicate number (the way I just described would push the number twice if there were three copies of it, whereas mine will push just once)

#Initialize a hashmap
#Iterate through nums:
    #If the num key isn't already there
        #Create it with a value of 1
    #Else
        #Add a value of 1 to it
#Initialize a solutions array
#Iterate through the hashmap
    #If the frequency is greater than 1, push it to the solutions array
#Return the solutions array

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myHash = {}
        for num in nums:
            if (num not in myHash):
                myHash[num] = 1
            else:
                myHash[num] += 1
        solutionsArray = []
        for key in myHash:
            if (myHash[key] > 1):
                solutionsArray.append(key)
        return solutionsArray

ourSolution = Solution()
sampleNums = [4, 3, 1, 2, 2, 4, 5]
print(ourSolution.findDuplicates(sampleNums))
