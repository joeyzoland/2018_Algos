#https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

"""
 Delete duplicate nodes
 head could be None as well for empty list
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def RemoveDuplicates(head):
    if (head is None):
        return None
    elif (head.next is None):
        return head

    valuesArray = [head.data]
    current = head
    while(current.next is not None):
        duplicateFlag = False
        for i in range(0, len(valuesArray)):
            if (valuesArray[i] == current.next.data):
                current.next = current.next.next
                duplicateFlag = True
                break
        if (duplicateFlag == False):
            valuesArray.append(current.next.data)
            current = current.next
    return head

#Sample list
sampleHead = Node(6)
sampleFirst = Node(5)
sampleSecond = Node(2)
sampleThird = Node(6)
sampleFourth = Node(7)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleSecond.next = sampleThird
sampleThird.next = sampleFourth

#Using method from previous exercise to check this solution
def print_list(head):
    current = head
    while (current is not None):
        print (current.data)
        current = current.next

print("list before")
print_list(sampleHead)
print("list after")
print_list(RemoveDuplicates(sampleHead))
