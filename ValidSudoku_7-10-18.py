import math

#I did it!!!  Rather than limiting this function to only a 9 X 9 sudoku board, I believe it should work for any board; tested for several cases on a 4 X 4 and 16 X 16, and it also passes all 9 X 9 cases on LeetCode

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def boardLocator(x, y):
            #The number of sectors is equal to the length of the board's length on any given side; as an example, sectors are defined as follows for 2 X 2 and 3 X 3 sector boards, and I believe this can functon can handle any board (e.g., 4 X 4, 5 X 5, etc.)

            #0 | 1
            #-----
            #2 | 4

            #0 | 1 | 2
            #---------
            #3 | 4 | 5
            #---------
            #6 | 7 | 8

            squareRoot = int(math.sqrt(len(board)))
            yBoardAddition = squareRoot * math.floor(y / squareRoot)
            xBoardAddition = math.floor(x / squareRoot)
            return yBoardAddition + xBoardAddition

        #Could have went with a huge array, but I think it's more clear to use a hash map where the digit is the key and there is a hash with x, y, and board sets as the value
        masterMap = {}
        #Note: We're assuming the x is the same as the y, as this is a sudoku board
        for i in range(1, len(board) + 1):
            masterMap[i] = {"x": set(), "y": set(), "sector": set()}
        for y in range(0, len(board)):
            for x in range(0, len(board)):
                if board[y][x] != ".":
                    currentDigit = int(board[y][x])
                    sector = boardLocator(x, y)
                    if (x in masterMap[currentDigit]["x"]) or (y in masterMap[currentDigit]["y"]) or (sector in masterMap[currentDigit]["sector"]):
                        return False
                    masterMap[currentDigit]["x"].add(x)
                    masterMap[currentDigit]["y"].add(y)
                    masterMap[currentDigit]["sector"].add(sector)
        return True

#This is the basic test given with the LeetCode problem
sampleBoard = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

sampleBoard1 = [[".", ".","2","."],
                ["1","2","3","4"],
                [".",".",".","1"],
                ["2","3","1","."]]
                #Fails due to 1's in bottom-right corner box

sampleBoard2 = [[".", ".","2","."],
                ["1","2","1","4"],
                [".",".",".","."],
                ["2","3","1","."]]
                #Fails due to 1's in 3rd column, index 2

sampleBoard3 = [[".", ".","2","."],
                ["3","2","1","4"],
                [".",".",".","."],
                ["1","3","1","."]]
                #Fails due to 1's in 4th row, index 3

sampleBoard4 = [["4","1","2","3"],
                ["3","2","1","4"],
                ["1","4","3","2"],
                ["2","3","4","1"]]
                #Valid

sampleBoard5 = [["4",".",".",".",".",".",".",".",".",".",".",".",".",".",".","4"],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
            #Invalid due to 4's in the top row

sampleBoard6 = [[".","16",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".","16",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
            #Invalid due to 16's in the leftmost row

sampleBoard7 = [["12",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".","12",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
            #Invalid due to 12's in the top-left box

sampleBoard8 = [['1','5','9','13','2','6','10','14','3','7','11','15','4','8','12','16'],
['2','6','10','14','3','7','11','15','4','8','12','16','5','9','13','1'],
['3','7','11','15','4','8','12','16','5','9','13','1','6','10','14','2'],
['4','8','12','16','5','9','13','1','6','10','14','2','7','11','15','3'],
['5','9','13','1','6','10','14','2','7','11','15','3','8','12','16','4'],
['6','10','14','2','7','11','15','3','8','12','16','4','9','13','1','5'],
['7','11','15','3','8','12','16','4','9','13','1','5','10','14','2','6'],
['8','12','16','4','9','13','1','5','10','14','2','6','11','15','3','7'],
['9','13','1','5','10','14','2','6','11','15','3','7','12','16','4','8'],
['10','14','2','6','11','15','3','7','12','16','4','8','13','1','5','9'],
['11','15','3','7','12','16','4','8','13','1','5','9','14','2','6','10'],
['12','16','4','8','13','1','5','9','14','2','6','10','15','3','7','11'],
['13','1','5','9','14','2','6','10','15','3','7','11','16','4','8','12'],
['14','2','6','10','15','3','7','11','16','4','8','12','1','5','9','13'],
['15','3','7','11','16','4','8','12','1','5','9','13','2','6','10','14'],
['16','4','8','12','1','5','9','13','2','6','10','14','3','7','11','15']]
            #Valid

mySolution = Solution()
print("case0:", mySolution.isValidSudoku(sampleBoard))
print("case1:", mySolution.isValidSudoku(sampleBoard1))
print("case2:", mySolution.isValidSudoku(sampleBoard2))
print("case3:", mySolution.isValidSudoku(sampleBoard3))
print("case4:", mySolution.isValidSudoku(sampleBoard4))
print("case5:", mySolution.isValidSudoku(sampleBoard5))
print("case6:", mySolution.isValidSudoku(sampleBoard6))
print("case7:", mySolution.isValidSudoku(sampleBoard7))
print("case8:", mySolution.isValidSudoku(sampleBoard8))



#This is the code that I used to make a the valid 16X16 grid; I'll probably generalize it later and make it its own function :)
# counter = 1
# sampleCaseGenerator = []
# for i in range(0, 16):
#     sampleCaseGenerator.append([])
#     counter = 0
#     for j in range(0, 16):
#         if (j%4==0):
#             counter += 1
#         sampleCaseGenerator[i].append(str(((i+counter) % 16) + 1))
#         counter += 4
# print(sampleCaseGenerator)



# #Archived code, only works with 3 X 3
# import math
#
# class Solution:
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         #Could have went with a huge array, but I think it's more clear to use a hash map where the digit is the key and there is a hash with x, y, and board sets as the value
#         def boardLocator(x, y):
#             if y < 3:
#                 boardAddition = 1
#             elif y < 6:
#                 boardAddition = 4
#             else:
#                 boardAddition = 7
#             return (math.floor(x / 3) + boardAddition)
#
#         masterArray = {}
#         for i in range(1, 10):
#             masterArray[i] = {"x": set(), "y": set(), "sector": set()}
#         for y in range(0, 9):
#             for x in range(0, 9):
#                 if board[y][x] != ".":
#                     currentDigit = int(board[y][x])
#                     sector = boardLocator(x, y)
#                     if (x in masterArray[currentDigit]["x"]) or (y in masterArray[currentDigit]["y"]) or (sector in masterArray[currentDigit]["sector"]):
#                         return False
#                     masterArray[currentDigit]["x"].add(x)
#                     masterArray[currentDigit]["y"].add(y)
#                     masterArray[currentDigit]["sector"].add(sector)
#         return True
