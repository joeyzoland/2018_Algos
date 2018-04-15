#https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    if (head is None):
        return 0
    tracker = [head]
    current = head.next
    #The below loop runs until either the current node matches the address of a node already recorded in the tracker array, or no such match has been found and current's .next pointer points to None
    while (current is not None):
        for i in range(0, len(tracker)):
            if (current == tracker[i]):
                return 1
        tracker.append(current)
        current = current.next
    return 0

#Sample list
sampleHead = Node(6)
sampleFirst = Node(5)
sampleSecond = Node(2)
sampleThird = Node(6)
sampleHead.next = sampleFirst
sampleFirst.next = sampleSecond
sampleSecond.next = sampleThird
sampleThird.next = sampleHead

print(has_cycle(sampleHead))
