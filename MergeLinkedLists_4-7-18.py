#https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

"""
 Merge two linked lists
 head could be None as well for empty list
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

# def MergeLists(headA, headB):
#     realHead = headA
#     lastSorted = None
#
#     leastPrior = None
#     leastValue = headA.data
#
#     while (current.next is not None):
#         if (current.next.data < leastA.data)
#             leastPrior = current
#             leastValue = current.next.data
#     #If the original head really has the lowest value
#     if (leastPrior == None):
#         if (lastSorted == None):
#             lastSorted = realHead
#         else:

def sortList(firstNode, previous=None):
    def print_list(head):
        current = head
        while (current is not None):
            print (current.data)
            current = current.next
    if (previous == None):
        realFirstNode = firstNode
        leastPrior = None
        leastNode = firstNode
        current = firstNode
        while (current.next is not None):
            if (current.next.data < leastNode.data):
                leastPrior = current
                leastNode = current.next
            current = current.next
        if (leastPrior is None):
            print_list(realFirstNode)
            sortList(firstNode.next, firstNode)
        else:
            leastPrior.next = leastPrior.next.next
            leastNode.next = firstNode
            realFirstNode = leastNode
            print_list(realFirstNode)
            sortList(leastNode.next, leastNode)
        return realFirstNode
    else:
        #If there is more than one node remaining...
        if (firstNode.next != None):
            leastPrior = previous
            leastNode = firstNode
            current = firstNode
            while (current.next is not None):
                if (current.next.data < leastNode.data):
                    leastPrior = current
                    leastNode = current.next
                current = current.next
            if (leastPrior == previous):
                print("route 1")
                print_list(leastNode)
                sortList(firstNode.next, firstNode)
            else:
                print("route 2")
                leastPrior.next = leastPrior.next.next
                leastNode.next = firstNode
                previous.next = leastNode
                print_list(leastNode)
                sortList(leastNode.next, leastNode)

#Sample list
sampleHead = Node(6)
sampleFirst = Node(5)
sampleSecond = Node(2)
sampleThird = Node(3)
sampleFourth = Node(4)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleSecond.next = sampleThird
sampleThird.next = sampleFourth

#Using method from previous exercise to check this solution
def print_list(head):
    current = head
    while (current is not None):
        print (current.data)
        current = current.next

print("list before")
print_list(sampleHead)
print("")
newHead = sortList(sampleHead)
print("list after")
print_list(newHead)
