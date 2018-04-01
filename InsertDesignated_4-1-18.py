#https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):
    newNode = Node(data)
    if (position == 0):
        newNode.next = head
        return newNode
    else:
        counter = 1
        current = head
        while (counter < position):
            current = current.next
            counter += 1
        newNode.next = current.next
        current.next = newNode
        return head

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
newSampleHead = InsertNth(sampleHead, 2, 4)
print_list(newSampleHead)
