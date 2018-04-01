#https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(oldHead, newHeadVal):
    newHead = Node(newHeadVal)
    if (oldHead is None):
        newHead.next = None
    else:
        newHead.next = oldHead
    return newHead

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

print("list before")
print_list(sampleHead)
print("list after")
newSampleHead = Insert(sampleHead, 2)
print_list(newSampleHead)
