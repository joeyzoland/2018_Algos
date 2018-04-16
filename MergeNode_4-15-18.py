#https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

"""
 Find the node at which both lists merge and return the data of that node.
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def FindMergeNode(headA, headB):
    if (headA == headB):
        return headA
    listA = [headA]
    listB = [headB]
    currentA = headA.next
    currentB = headB.next
    while (currentA is not None or currentB is not None):
        if (currentA is not None):
            for i in range(0, len(listB)):
                if (currentA == listB[i]):
                    return currentA.data
            listA.append(currentA)
            currentA = currentA.next
        if (currentB is not None):
            for j in range(0, len(listA)):
                if (currentB == listA[j]):
                    return currentB.data
            listB.append(currentB)
            currentB = currentB.next
    return("Error: Both lists should converge at some point, but do not")

#Sample list
sampleHead = Node(6)
sampleFirst = Node(5)
sampleSecond = Node(2)
sampleThird = Node(7)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleSecond.next = sampleThird

#Sample list2
sampleHead2 = Node(1)
sampleFirst2 = Node(9)
sampleHead2.next = sampleFirst2
sampleFirst2.next = sampleThird

print(FindMergeNode(sampleHead, sampleHead2))
