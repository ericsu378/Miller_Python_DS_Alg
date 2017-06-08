__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

from ch3_DataStructures import Stack
import unittest

class TestExamples(unittest.TestCase):

    def test_parChecker(self):
        self.test_str_true = ('{{([][])}()}')
        self.test_str_false = ('[{()]')
        self.assertEqual(parChecker(self.test_str_true), True)
        self.assertEqual(parChecker(self.test_str_false), False)


def parChecker(symbolString):
    """
    This function checks to see if parentheses  in a 'symbolString' is balanced or not
    :param symbolString: input string
    :return: True if balanced, False otherwise
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    """
    Helper function for parChecker. Checks if 'open' and 'close' are of the same type
    :param open: open symbol
    :param close: close symbol
    :return: True if open symbol type = close symbol type, False otherwise
    """
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

def main():
    print(parChecker('{{([][])}()}'))
    print(parChecker('[{()]'))

if __name__ == '__main__':
    # unittest.main()
    main()