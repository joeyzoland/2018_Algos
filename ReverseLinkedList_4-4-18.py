#https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

"""
 Reverse a linked list
 head could be None as well for empty list
"""

#Note: Created a new list for the solution.  In the future, may want to modify the list in place instead.

class Node(object):

    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

def Reverse(head):
    if (head == None):
        return None
    elif (head.next == None):
        return head
    while (head.next != None):
        current = head
        #Looking for the second-to-last node in given list, so we can use its .next to access the last node
        while (current.next.next != None):
            current = current.next
        #If newHead isn't defined, make it the last node of the given list, then cut off its connection in the given list
        if ("newHead" not in locals()):
            newHead = current.next
            current.next = None
            current2 = newHead
        #If newHead has already been defined, add the last node from the given list to the end of the list that we are creating, update current2 to have the last node of the list that we are creating, and cut off its connection from the given list
        else:
            current2.next = current.next
            current2 = current2.next
            current.next = None
    #Add the head of the given list to th end of the list we are creating
    current2.next = head
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

print("list in normal order")
print_list(sampleHead)
print("list after reversing order")
print_list(Reverse(sampleHead))
