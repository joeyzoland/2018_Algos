#https://leetcode.com/problems/combinations/description/

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def combineHelper(counter, currentList):
            if len(currentList) == k:
                result.append(currentList)
                return
            elif (counter > n):
                return
            else:
                copy = currentList[:]
                copy.append(counter)
                copy2 = currentList[:]
                combineHelper(counter + 1, copy)
                combineHelper(counter + 1, copy2)
        combineHelper(1, [])
        return result

mySolution = Solution()
print(mySolution.combine(4, 2))
