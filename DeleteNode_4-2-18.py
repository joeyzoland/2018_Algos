#https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

"""
 Delete Node at a given position in a linked list
"""

class Node(object):
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Delete(head, position):
    if (position == 0):
        return head.next
    else:
        current = head
        counter = 1
        while (counter < position):
            current = current.next
            counter += 1
        current.next = current.next.next
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
newSampleHead = Delete(sampleHead, 1)
print_list(newSampleHead)
