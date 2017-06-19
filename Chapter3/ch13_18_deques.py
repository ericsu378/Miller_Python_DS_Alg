__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

from ch3_DataStructures import Deque
import unittest

class TestExamples(unittest.TestCase):

    def test_pal_checker_false(self):
        input_str = "lsdkjfskf"
        self.assertFalse(pal_checker(input_str))

    def test_pal_checker_true(self):
        input_str = "radar"
        self.assertTrue(pal_checker(input_str))


def pal_checker(input_str):
    char_deque = Deque()

    for ch in input_str:
        char_deque.addRear(ch)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            still_equal = False

        return still_equal


def main():
    print(pal_checker("lsdkjfskf"))
    print(pal_checker("radar"))

if __name__ == '__main__':
    # unittest.main()
    main()