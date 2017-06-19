__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

from ch3_DataStructures import Stack
import unittest

# class TestExamples(unittest.TestCase):
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


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        """
        find item and link around node to remove it
        :return:
        """
        current = self.head
        previous = None
        while current.getData() != item:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def index(self, item):
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
    mylist = OrderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    # mylist = [17, 26, 31, 54, 77, 93]
    print("Added:[54, 26, 93, 17, 77, 31] | mylist.size = {} | mylist.search(93) = {} | mylist.search(100) = {}".format(
        mylist.size(), mylist.search(93), mylist.search(100)))


    mylist.add(100)
    # mylist = [17, 26, 31, 54, 77, 93, 100]
    print("Added: '100' | mylist.size = {} | mylist.search(100) = {}".format(
        mylist.size(), mylist.search(100)))


    mylist.remove(54)
    # mylist = [17, 26, 31, 77, 93, 100]
    mylist.remove(93)
    # mylist = [17, 26, 31, 77, 100]
    mylist.remove(31)
    # mylist = [17, 26, 77, 100]
    print("Removed: '54', '93', '31' | mylist.size() = {} | mylist.search(31) = {} | mylist.index(100) = {}".format(
        mylist.size(), mylist.search(31), mylist.index(100)))

    mylist.pop(2)
    # mylist = [17, 26, 100]
    print("Pop(2) | mylist.size() = {} | mylist.search(77) = {} | mylist.index(77) = {} | mylist.index(100) = {}".format(
        mylist.size(), mylist.search(77), mylist.index(77), mylist.index(100)))

    mylist.pop()
    # mylist = [17, 26]
    print("Pop() | mylist.size() = {} | mylist.search(100) = {} | mylist.index(100) = {}".format(
        mylist.size(), mylist.search(100), mylist.index(100)))


if __name__ == '__main__':
    # unittest.main()
    main()