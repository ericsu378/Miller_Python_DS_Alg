__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# 3.27 Programming Exercises:
# 5) Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.
# 7) It is possible to implement a queue such that both enqueue and dequeue have O(1)
#    performance on average. In this case it means that most of the time enqueue and
#    dequeue will be O(1) except in one particular circumstance where dequeue will be O(n)

import unittest

class MyTest(unittest.TestCase):
    def test_revstring(self):
        self.assertEqual(revstring('apple'),'elppa')
        self.assertEqual(revstring('x'),'x')
        self.assertEqual(revstring('1234567890'),'0987654321')


# Implement a 'Stack' in python
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items) - 1]

     def size(self):
         return len(self.items)

     def return_obj(self):
         return self.items


# Implement a 'Queue' in Python
# -----------------------------------------------
# Rear (enqueue) ================= Front (deque)
# -----------------------------------------------
class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "Q1"

    def isEmpty(self): # O(1)
        return self.items == []

    def enqueue(self, item): # O(n)
        self.items.insert(0, item)

    def dequeue(self): # O(1)
        return self.items.pop()

    def size(self): # O(1)
        return len(self.items)

    def return_obj(self):
        return self.items

# Implement a 'DeQueue' in Python
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def return_obj(self):
        return self.items

# 5) Implement the Queue ADT, using a list such that the rear of the queue is at the end of the list.
# -----------------------------------------------
# Front (deque) ================= Rear (enqueue)
# -----------------------------------------------
class Queue_v2:
    def __init__(self):
        self.items = []

    def isEmpty(self): # O(1)
        return self.items == []

    def enqueue(self, item): # O(1)
        self.items.append(item)

    def dequeue(self): # O(k or n)
        return self.items.pop(0)

    def size(self): # O(1)
        return len(self.items)

    def return_obj(self):
        return self.items

# 7) It is possible to implement a queue such that both enqueue and dequeue have O(1)
#    performance on average. In this case it means that most of the time enqueue and
#    dequeue will be O(1) except in one particular circumstance where dequeue will be O(n)
#    Answer: Yes, when you utilize a linked list that has knowledge of both the head and tail.

#   Queue_linked_list should be finished. just need to test!!! and done wiht 7
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

class Queue_linked_list:
    """
    See ch3_13_queues for benchmark test
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def isEmpty(self): # O(1)
        return self.count == 0

    def enqueue(self, item): # O(1)
        temp = Node(item)
        temp.setNext(None)
        if self.head is None:
            self.head = temp
            self.tail = self.head
        else:
            self.tail.setNext(temp)
            self.tail = self.tail.getNext()
        self.count += 1

    def dequeue(self): # O(1)
        # Check if queue is empty
        if self.isEmpty():
            print("Queue is Empty!")
            return None
        temp = self.head
        # Case when self.head == self.tail
        if self.head == self.tail:
            self.front = None
            self.tail = None
        # Normal case
        else:
            self.head = self.head.getNext()
        self.count -= 1
        return temp

    def size(self): # O(1)
        return self.count


# Write a function revstring(mystr) that uses a stack to reverse the characters in a string
def revstring(mystr):
    """
    Uses the stack data structure to return a reversed character mystr
    :param mystr: a string
    :return: reversed 'mystr'
    """

    # initialize
    stack = Stack()
    returnString = []

    # put each character into stack
    for character in mystr:
        stack.push(character)

    # retrieve each character in stack and append to a list

    # old code
    # for item in range(stack.size()):
    #     returnString.append(stack.pop())
    # return ''.join(returnString)

    returnString = ''
    while not stack.isEmpty():
        returnString = returnString + stack.pop()
    return returnString

def main():
    pass


if __name__ == '__main__':
    unittest.main()
    # main()


