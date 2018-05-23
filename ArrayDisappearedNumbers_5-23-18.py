#LeetCode
#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

#[2,1,2,3,6]

#[1,2,2,3,6]
# ^
#Is this 1, check!

#[1,2,2,3,6]
#   ^
#Is this 2, check!

#[1,2,2,3,6]
#     ^
#Is this 3, no
#Is it less than 3, yes, so move up your index

#[1,2,2,3,6]
#       ^
#Is this 3, check!

#[1,2,2,3,6]
#         ^
#Is this 4, no
#Is is less than 4, no, so push it and increment your number

#[1,2,2,3,6]
#         ^
#Is this 5, no
#Is is less than 5, no, so push it and increment your number

#Loop stops because number = 6, and 6 is greater than length of array




#Sort the list
#Initialize a number variable, index variable, and missingArray variable
#While the index variable is less than the length of the list and the number variable is less than the length of the list
    #If the array's character matches the number variable
        #Increment both the number and index variables
    #If the array's character is greater than the number
        #Push the number to your missingArray
        #Increment the number
    #If the array's character is less than the number
        #Increment the index
#Check all of the numbers including number all the way through the length of the list, and use a for loop to push them all into the missingArray
#Return the missingArray

#Note upon completion: Other LeetCode users used Python's "in" operator on the raw array instead of sorting to search for each number, and it was considerably faster

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        number = 1
        index = 0
        missingArray = []
        while(index < len(nums) and number <= len(nums)):
            if(nums[index] == number):
                number += 1
                index += 1
            elif(nums[index] > number):
                missingArray.append(number)
                number += 1
            elif(nums[index] < number):
                index += 1
        for missingNumber in range(number, len(nums) + 1):
            missingArray.append(missingNumber)
        return missingArray

ourSolution = Solution()
sampleArray = [3, 2, 2, 2]
print(ourSolution.findDisappearedNumbers(sampleArray))
