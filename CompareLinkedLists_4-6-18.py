#https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

"""
 Compare two linked lists
 Head could be None as well for empty list
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

#Returns 1 for equal lists and 0 for unequal lists
def CompareLists(headA, headB):
    current1 = headA
    current2 = headB
    #Keep iterating until one or both of current1 and current2 are None
    while (current1 is not None and current2 is not None):
        if (current1.data != current2.data):
            return 0
        else:
            current1 = current1.next
            current2 = current2.next
    #If the last loop finished and both are None, you know the lists are equal because everything before the list's ends are equal; otherwise, you know that only one of the two lists.nexts is currently None, so they are unequal
    if (current1 is None and current2 is None):
        return 1
    return 0

#Sample list
sampleHead = Node(3)
sampleFirst = Node(4)
sampleSecond = Node(5)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond

#Sample list2
sampleHead2 = Node(3)
sampleFirst2 = Node(4)
sampleSecond2 = Node(5)
sampleHead2.next = sampleFirst2
sampleFirst2.next = sampleSecond2

#Sample list3
sampleHead3 = Node(3)
sampleFirst3 = Node(4)
sampleSecond3 = Node(6)
sampleHead3.next = sampleFirst3
sampleFirst3.next = sampleSecond3

#Sample list4
sampleHead4 = Node(3)

#Sample list5
sampleHead5 = Node(3)
sampleFirst5 = Node(4)
sampleHead5.next = sampleFirst5

print(CompareLists(sampleHead, sampleHead2))
