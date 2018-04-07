#https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

"""
 Merge two linked lists
 head could be None as well for empty list
"""

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
