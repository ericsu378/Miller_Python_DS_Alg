__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

from ch3_DataStructures import Stack
import unittest

class TestExamples(unittest.TestCase):
    def test_baseConverter1(sself):
        self.assertEqual(baseConverter(25, 2), '11001')

    def test_find_pivot(self):
        self.assertEqual(baseConverter(25, 16), '19')

def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

def main():
    print(baseConverter(25, 2))
    print(baseConverter(25, 16))

if __name__ == '__main__':
    # unittest.main()
    main()