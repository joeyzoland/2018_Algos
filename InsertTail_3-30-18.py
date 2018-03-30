#https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 return back the head of the linked list in the below method
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    if (head is None):
        head = Node(data)
    else:
        current = head
        while (current.next is not None):
            current = current.next
        current.next = Node(data)
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
Insert(sampleHead, 6)
print_list(sampleHead)
