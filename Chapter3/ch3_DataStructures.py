__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

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
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
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


