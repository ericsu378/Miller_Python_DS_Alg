__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# 3.21 Self Check - Part II:
# In the previous problem, you most likely created an append method that was O(n).
# If you add an instance variable to the UnorderedList class you can create an
# an append method that is O(1). Modify your append method to be O(1).

from ch3_DataStructures import Stack
import unittest

# class TestExamples(unittest.TestCase):


# Implement an Unordered List: Linked List in Python
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

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        if self.tail == None:
            self.tail = temp

        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                # Ensures self.tail is updated if self.tail is removed
                if current.getData() == self.tail.getData():
                    self.tail = previous
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.tail
        temp = Node(item)
        temp.setNext(None)
        current.setNext(temp)

    def insert(self, item, idx):
        """
        inserts 'item' in specified 'idx' in linked list
        - traverse linked list for 'idx' nodes and inserts new node after
        :param item:
        :param location:
        :return:
        """
        current = self.head
        count = 0
        while count < idx:
            current = current.getNext()
            count = count + 1
        temp = Node(item)
        temp.setNext(current.getNext())
        current.setNext(temp)

    def index(self, item):
        """
        traverses linked list and returns location of item in linked list
        :param item:
        :return:
        """
        current = self.head
        count = 0
        found = False
        if self.search(item):
            while current != None and not found:
                if current.getData() == item:
                    found = True
                else:
                    current = current.getNext()
                    count = count + 1
            return count
        else:
            return False

    def pop(self, idx = None):
        """
        removes and returns node value at 'idx' from linked list
        :param idx:
        :return:
        """
        current = self.head
        count = 0
        previous = None
        if idx is None:
            idx = self.size() - 1
        while count < idx:
            previous = current
            current = current.getNext()
            count = count + 1

        # Remove Node
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        # Return data
        return current.getData()





def main():

    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    # mylist = [54, 26, 93, 17, 77, 31]
    print("Added:[54, 26, 93, 17, 77, 31] | mylist.size = {} | mylist.search(93) = {} | mylist.search(100) = {}".format(
        mylist.size(), mylist.search(93), mylist.search(100)))


    mylist.add(100)
    # mylist = [100, 54, 26, 93, 17, 77, 31]
    print("Added: '100' | mylist.size = {} | mylist.search(100) = {}".format(
        mylist.size(), mylist.search(100)))


    mylist.remove(54)
    # mylist = [100, 26, 93, 17, 77, 31]
    mylist.remove(93)
    # mylist = [100, 26, 17, 77, 31]
    mylist.remove(31)
    # mylist = [100, 26, 17, 77]
    print("Removed: '54', '93', '31' | mylist.size() = {} | mylist.search(93) = {}".format(
        mylist.size(), mylist.search(93)))


    mylist.append(50)
    # mylist = [100, 26, 17, 77, 50]
    print("Appended: '50' | mylist.size() = {} | mylist.search(50) = {}".format(
        mylist.size(), mylist.search(50)))


    mylist.insert(21, 2)
    # mylist = [100, 26, 17, 21, 77, 50]
    print("Inserted '21' at idx = 2 | mylist.size() = {} | mylist.search(21) = {} | mylist.index(21) = {}".format(
        mylist.size(), mylist.search(21), mylist.index(21)))


    mylist.pop(3)
    # mylist = [100, 26, 17, 77, 50]
    print("Pop(3) | mylist.size() = {} | mylist.search(21) = {} | mylist.index(21) = {} | mylist.index(50) = {}".format(
        mylist.size(), mylist.search(21), mylist.index(21), mylist.index(50)))

    mylist.pop()
    # mylist = [100, 26, 17, 77]
    print("Pop() | mylist.size() = {} | mylist.search(50) = {} | mylist.index(50) = {}".format(
        mylist.size(), mylist.search(50), mylist.index(50)))

    mylist.remove(77)
    # mylist = [100, 26, 17, 77]
    print("Remove(77) | mylist.size() = {} | mylist.search(77) = {} | mylist.index(77) = {}".format(
        mylist.size(), mylist.search(77), mylist.index(77)))

if __name__ == '__main__':
    # unittest.main()
    main()

