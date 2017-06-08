__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

from ch3_DataStructures import Stack
import unittest

class TestExamples(unittest.TestCase):

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix("A * B + C * D"), 'A B * C D * +' )
        self.assertEqual(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"), 'A B + C * D E - F G + * -')

    def test_postfix_eval(self):
        self.assertEqual(postfix_eval('7 8 + 3 2 + /'), 3.0)

    def test_do_math(self):
        self.assertEqual(do_math("*", 3, 4), 12)
        self.assertEqual(do_math("/", 9, 3), 3)
        self.assertEqual(do_math("+", 3, 4), 7)
        self.assertEqual(do_math("-", 5, 3), 2)


def infix_to_postfix(infix_expr):
    """
    Stack: 'op_stack' holds operators
    List: 'postfix_list' holds output
    Dict: 'prec' holds precedence values for operators
    Logic -
        1) use op_stack to keep operators
        2) assign precedence value to operators
        3) scan token list from left to right
              if token is:
                3a) an operand - append to end of 'postfix_list'
                3b) '(' - push on 'op_stack'
                3c) ')' - pop 'op_stack' until corresponding left
                          parenthesis is removed & append to 'postfix_list'
                3d) an operator - push onto 'op_stack' but first remove any
                                  operators on 'op_stack' with >= precedence
                                  & append to 'postfix_list'
        4) pop and append any remaining operators from 'op_stack' to 'postfix_list'
    :param infix_expr: Input infix string
    :return: postfix string
    """

    # Assign precedence values to operators
    prec = {}
    prec['**'] = 4
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:

        if not op_stack.isEmpty():
            print("token = {}, stack_peek = {}".format(token, op_stack.peek()))
        else:
            print("token = {}".format(token))

        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.isEmpty()) and \
                    (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

def postfix_eval(postfix_expr):
    """
    Stack: 'operand_stack' holds operands
    Logic -
        1) use 'operand_stack' to hold operands
        2) scan token list from left to right
            if token is:
                2a) an operand - convert from str --> int and push onto stack
                2b) an operator - pop stack twice, first pop is second operand,
                                  perform operation and push result back to stack
        3) pop stack to return final value
    :param postfix_expr: postfix expression string
    :return: evaluated value
    """
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(operator, op1, op2):
    """
    Helper function to do mathematical operations */+-
    :param operator: string
    :param op1: int
    :param op2: int
    :return: evaluated expression int
    """
    if operator == "*":
        return op1 * op2
    if operator == "/":
        return op1 / op2
    if operator == "+":
        return op1 + op2
    if operator == "-":
        return op1 - op2

def main():
    print(infix_to_postfix("5 * 3 ** ( 4 - 2 )"))

if __name__ == '__main__':
    # unittest.main()
    main()