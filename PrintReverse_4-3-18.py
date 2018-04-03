#https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def ReversePrint(head):
    if (head == None):
        return None
    else:
        current = head
        #This solution uses an array, as it takes slightly more memory but reduces time complexity compared to iterating through the singly linked list and printing the last item, iterating through the list and printing out the second to last item, etc.
        solutionsArray = []
        while (current != None):
            solutionsArray.append(current.data)
            current = current.next
        #Got mixed results on whether this should be "range" or "xrange"
        for i in xrange(len(solutionsArray) - 1, -1, -1):
            print (solutionsArray[i])

#Sample list
sampleHead = Node(3)
sampleFirst = Node(4)
sampleSecond = Node(5)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond

#Using method from previous exercise to check this solution
def print_list(head):
    current = head
    while (current is not None):
        print (current.data)
        current = current.next

print("list in normal order")
print_list(sampleHead)
print("list in reverse order")
ReversePrint(sampleHead)
