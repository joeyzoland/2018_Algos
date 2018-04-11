#https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def GetNode(head, position):
    if (head is None):
        return 0

    #Use this loop to get the length of the linked list, as we need this to calculate our "TruePosition", which is the variable we use to count from the front, since the given variable "position" counts from the back
    length = 1
    current = head
    while (current.next is not None):
        current = current.next
        length += 1
    #Have to subtract an additional 1 due to indexing, since we're counting the position starting from the tail, with the tail being 1
    truePosition = length - position - 1

    counter = 0
    current = head
    while (counter < truePosition):
        current = current.next
        counter += 1
    return current.data

#Sample list
sampleHead = Node(2)
sampleFirst = Node(1)
sampleSecond = Node(3)
sampleThird = Node(5)
sampleFourth = Node(6)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleSecond.next = sampleThird
sampleThird.next = sampleFourth

print(GetNode(sampleHead, 4))
