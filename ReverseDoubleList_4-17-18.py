#https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

"""
 Reverse a doubly linked list
 head could be None as well for empty list
"""

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

def Reverse(head):
    if (head is None):
        return None
    elif (head.next is None):
        return head
    else:
        #First, we iterate to the end of the list, as that will be our new head
        current = head
        while (current.next is not None):
            current = current.next
        newHead = current
        #We use lastCurrent to keep track of the last node in the list
        lastCurrent = current
        #What we are doing is taking any nodes before our newHead, as newHead was the last node in our original list, and removing them to put them at the end of our new list
        while (newHead.prev is not None):
            #We keep track of the newLastNode that was right before newHead, and then we redo the connections on both sides such that newHead is connected to the node before that newLastNode, and that node before newLastNode is connected to newHead (if there is one)
            newLastNode = newHead.prev
            newHead.prev = newHead.prev.prev
            if (newHead.prev is not None):
                newHead.prev.next = newHead
            #Finally, we add that node before newHead to the end of the list and complete the connections on both sides, not forgetting to remove newLastNode's connection to newHead, as newLastNode is now at the end of the list and is connected to None
            lastCurrent.next = newLastNode
            newLastNode.prev = lastCurrent
            newLastNode.next = None
            lastCurrent = lastCurrent.next
        return newHead

#Sample list
sampleHead = Node(2)
sampleFirst = Node(4)
sampleSecond = Node(6)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleFirst.prev = sampleHead
sampleSecond.prev = sampleFirst

#Demo of the Reverse function on this list
#Start: 2, 4, 6
#First Iteration: 2, 6, 4
#Second Iteration: 6, 4, 2

#Using method from previous exercise to check this solution
def print_list(head):
    current = head
    while (current is not None):
        print (current.data)
        current = current.next

print("Before...")
print_list(sampleHead)
print("After...")
print_list(Reverse(sampleHead))
