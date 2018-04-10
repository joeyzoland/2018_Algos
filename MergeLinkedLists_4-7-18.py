#https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

"""
 Merge two linked lists
 head could be None as well for empty list
"""

#Note: I originally thought this challenge wanted to merge two UNSORTED lists in ascending order, whereas the two lists are actually already sorted in this hackerRank challenge.  Haha!  It was great practice to sort the individual lists before the merge anyways...

class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def MergeLists(headA, headB):
    def sortList(firstNode, previous=None):
        if (firstNode is None):
            return None
        elif (previous == None):
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
                sortList(firstNode.next, firstNode)
            else:
                leastPrior.next = leastPrior.next.next
                leastNode.next = firstNode
                realFirstNode = leastNode
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
                    sortList(firstNode.next, firstNode)
                else:
                    leastPrior.next = leastPrior.next.next
                    leastNode.next = firstNode
                    previous.next = leastNode
                    sortList(leastNode.next, leastNode)
    newHeadA = sortList(headA)
    newHeadB = sortList(headB)

    #If the first and second lists are None, we should return None; otherwise, if only one is None, we should return the other list because it is already "merged" since there is nothing to merge it with
    if (newHeadA is None):
        if (newHeadB is None):
            return None
        return newHeadB
    elif(newHeadB is None):
        return newHeadA

    #We are going to have two loops, but we want to identify which list has the lowest starting value so we can start with it
    if (newHeadA.data < newHeadB.data):
        firstList = newHeadA
        secondList = newHeadB
    else:
        firstList = newHeadB
        secondList = newHeadA

    current1 = firstList
    current2 = secondList
    while (current1.next is not None and current2 is not None):
        if (current2.data < current1.next.data):
            mergingNode = current2
            #Hold the new current2 node in memory, as we are about to disconnect the previous node from it and we would lose it in memory
            current2 = current2.next
            mergingNode.next = current1.next
            current1.next = mergingNode
        else:
            current1 = current1.next
    #If we have leftovers in secondList after reaching the end of the firstList, then we have to add them to the end of firstList because that is our merged list
    if (current1.next is None):
        current1.next = current2
    return firstList



#Sample list
sampleHead = Node(6)
sampleFirst = Node(5)
sampleSecond = Node(2)
sampleThird = Node(3)
sampleFourth = Node(8)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleSecond.next = sampleThird
sampleThird.next = sampleFourth

#Sample list
sampleHead2 = Node(7)
sampleFirst2 = Node(4)
sampleSecond2 = Node(1)
sampleThird2 = Node(9)
sampleHead2.next = sampleFirst2
sampleFirst2.next = sampleSecond2
sampleSecond2.next = sampleThird2

#Using method from previous exercise to check this solution
def print_list(head):
    current = head
    while (current is not None):
        print (current.data)
        current = current.next

print("firstList")
print_list(sampleHead)
print("secondList")
print_list(sampleHead2)
print("After merge...")
print_list(MergeLists(sampleHead, sampleHead2))
