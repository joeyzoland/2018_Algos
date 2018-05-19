#LeetCode
#https://leetcode.com/problems/single-number/description/

#Iterate through the array
    #If the entry is not in your set, add it to your set
    #If it is not in your set, remove it from your set
#Grab the only element left in your set and return it; otherwise, return an error message

#Note, we are assuming that each number is given twice except for 1; if there was a number with more of a frequency than 2 or if the number of 1 frequency characters is not 1, it will return an error if there are no 1-frequencies and it will simply return the first if there are more than one 1-frequencies or odd-frequency characters

#[1, 2, 2]
#Set {1}
#Set (1, 2)
#Set (1)
#Print what is in set (answer = 1)

#Note: This could be done with no additional memory, but additional time complexity, by iterating through nums and, at each num, checking if there is another number of the same character; if you ever do not find another copy of that number, you could just return it

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ourSet = set()
        for num in nums:
            if (num not in ourSet):
                ourSet.add(num)
            else:
                ourSet.remove(num)
        for value in ourSet:
            return value

ourObject = Solution()
print(ourObject.singleNumber([2, 2, 1, 4, 1]))
