#https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
"""

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

def SortedInsert(head, data):
    if (head is None):
        newHead = Node(data)
        return newHead
    elif (data < head.data):
        newHead = Node(data)
        newHead.next = head
        head.prev = newHead
        return newHead
    current = head
    while (current.next is not None):
        if (current.next.data > data):
            newNode = Node(data)
            newNode.next = current.next
            newNode.prev = current
            current.next = newNode
            newNode.next.prev = newNode
            return head
        else:
            current = current.next
    #If the while loop completes, that means there is nothing in the list that is greater than data, so data should be added as the tail
    newNode = Node(data)
    current.next = newNode
    newNode.prev = current
    return head

#Sample list
sampleHead = Node(2)
sampleFirst = Node(4)
sampleSecond = Node(6)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleFirst.prev = sampleHead
sampleSecond.prev = sampleFirst

#Using method from previous exercise to check this solution
def print_list(head):
    current = head
    while (current is not None):
        print (current.data)
        current = current.next

print("Before...")
print_list(sampleHead)
print("After...")
print_list(SortedInsert(sampleHead, 1))
