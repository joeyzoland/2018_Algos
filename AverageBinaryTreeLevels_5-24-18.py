#leetcode
#https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

#Initialize a holding array with the first node in it
#(If there is no solutionsArray passed in, initialize it as an empty array)
#For every node in the holding array:
    #If there is a node on the left:
        #Push it to a new holding array
    #If there is a node on the right:
        #Push it to the new holding array
#If there are any nodes in the new holding array
    #Take the average of all node values in the holding array and push it to the solutions array
#Else:
    #return the solutions array
#Recursively run the function, passing in the new holding array


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def recursiveSearch(holdingArray, solutionsArray):
            newHoldingArray = []
            for node in holdingArray:
                if node.left is not None:
                    newHoldingArray.append(node.left)
                if node.right is not None:
                    newHoldingArray.append(node.right)
            if (len(newHoldingArray) != 0):
                toAppend = 0
                for newNode in newHoldingArray:
                    toAppend += newNode.val
                solutionsArray.append(float(toAppend / len(newHoldingArray)))
                #Overwriting holding array, as I don't want tons of old holdingArrays to be stored in memory in different scopes
                holdingArray = newHoldingArray
                return recursiveSearch(holdingArray, solutionsArray)
            else:
                return solutionsArray
        return recursiveSearch([root], [float(root.val)])

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(2)
firstFirstLevelNode = TreeNode(4)
secondFirstLevelNode = TreeNode(6)
firstSecondLevelNode = TreeNode(8)
secondSecondLevelNode = TreeNode(10)
firstThirdLevelNode = TreeNode(12)

root.left = firstFirstLevelNode
root.right = secondFirstLevelNode
root.left.left = firstSecondLevelNode
root.right.left = secondSecondLevelNode
root.left.left.left = firstThirdLevelNode

ourSolution = Solution()
print(ourSolution.averageOfLevels(root))
