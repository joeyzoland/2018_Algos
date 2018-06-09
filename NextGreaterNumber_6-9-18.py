#leetcode
#https://leetcode.com/problems/next-greater-element-i/description/

#Initialize solutions array
#Iterate through the first array
    #Iterate through the second array
        #Checking = False
        #Pushed = False
        #If the first array character matches the second array character
            #Checking = True
        #Else if Checking = True and second array character is bigger than first array character
            #Push that character to solutions array
            #Pushed = True
            #Break
    #If we get all the way through the loop and never pushed anything (Pushed = False), we want to push -1 to solutions
#Return solutions

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        solutionsArray = []
        for number1 in nums1:
            checking = False
            pushed = False
            for number2 in nums2:
                if (number1 == number2):
                    checking = True
                elif(checking == True and number2 > number1):
                    solutionsArray.append(number2)
                    pushed = True
                    break
            if (pushed == False):
                solutionsArray.append(-1)
        return solutionsArray

ourSolution = Solution()
sample1 = [4,1,2]
sample2 = [1,3,4,2]
print(ourSolution.nextGreaterElement(sample1, sample2))
