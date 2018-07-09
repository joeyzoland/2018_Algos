"""
https://leetcode.com/problems/employee-importance/description/

You are given a data structure of employee information, which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all his subordinates.



My PseudoCode / Diagramming
11

1 - > 2 - > 3
5     3     3
            p

If all employees are given a unique index number, and it looks like they're sorted, then you can find a given employee in the nested array via the employee's unique index number - 1 (because indexing starts at 0)

General recursive strategy:
if no subordinates, return (base case)
Else, run a for loop through all subordinates and run this function again on each of them, finding them in the nested array by unique id - 1 = index
"""

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

#Note: Below is the first solution using the array given, but it's incredibly wasteful to find the employee in an array, so the later solution below allows employees to be accessible via a map instead
# class Solution:
#     def getImportance(self, employees, id):
#         """
#         :type employees: Employee
#         :type id: int
#         :rtype: int
#         """
#         for potentialEmployee in employees:
#             if id == potentialEmployee.id:
#                 employee = potentialEmployee
#                 break
#         scopeSum = 0
#         for subordinate in employee.subordinates:
#             scopeSum += self.getImportance(employees, subordinate)
#         return employee.importance + scopeSum

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        map = {}
        for employee in employees:
            map[employee.id] = {"importance": employee.importance, "subordinates": employee.subordinates}
        # print (map)
        def importanceHelper(helperId):
            employee = map[helperId]
            # print (employee)
            # print (employee["subordinates"])
            scopeSum = 0
            for subordinate in employee["subordinates"]:
                scopeSum += importanceHelper(subordinate)
            return employee["importance"] + scopeSum
        return importanceHelper(id)



class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
Employee1 = Employee(1, 5, [2, 3])
Employee2 = Employee(2, 3, [])
Employee3 = Employee(3, 3, [])
sampleEmployees = [Employee1, Employee2, Employee3]
sampleId = 1

mySolution = Solution()
print(mySolution.getImportance(sampleEmployees, sampleId))
