#LeetCode
#https://leetcode.com/problems/max-area-of-island/description/

#Iterate through the array
    #Set a "land" variable to the result of a recursive function on each character
        #If it's not a 1, return 0
        #If it's a 1
            #Change the number to a 2 (so it won't be checked again)
            #return 1 + the recursive function in each of the four directions
    #If the "land" variable is greater than the solution, record the solution as the land variable
#After the loop is done, return the solution

#[[0, 1, 0],
# [1, 1, 1],
# [0, 0, 1]]

#[[0, 2, 0],
# [1, 1, 1],
# [0, 0, 1]]

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def adjacentLand(grid, x, y):
            #These two statements check if the specified input position is outside the bounds of the grid, so that it's actual character can be checked against the value of "1" to see if it's land in the third statement; note that it has to be done with separate statements, as the second and third statements can throw errors if the first statement's error condition is met (e.g., you can't check the x position within the y array for the second statement, if the y array is outside the bounds of the grid)
            if (y < 0 or y >= len(grid)):
                return 0
            elif (x < 0 or x >= len(grid[y])):
                return 0
            elif (grid[y][x] != 1):
                return 0
            else:
                grid[y][x] = 2
                return 1 + adjacentLand(grid, x-1, y) + adjacentLand(grid, x+1, y) + adjacentLand(grid, x, y-1) + adjacentLand(grid, x, y+1)

        solution = 0
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                current = adjacentLand(grid, x, y)
                if (current > solution):
                    solution = current
        return solution

ourSolution = Solution()
sampleGrid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]

print(ourSolution.maxAreaOfIsland(sampleGrid))
