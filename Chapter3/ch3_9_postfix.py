__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# 3.27 Programming Exercises:
# 1) Modify the infix-to-postfix algorithm so that it can handle errors.
# 2) Modify the postfix evaluation algorithm so that it can handle errors.
# 3) Implement a direct infix evaluator that combines the functionality of infix-to-postfix
#    conversion and the postfix evaluation algorithm. Your evaluator should process infix
#    tokens from left to right and use two stacks, one for operators and one for operands,
#    to perform the evaluation.
# 4) Turn your direct infix evaluator from the previous problem into a calculator.

from ch3_DataStructures import Stack
import unittest
import sys
import logging

# class TestExamples(unittest.TestCase):
#
#     def test_infix_to_postfix(self):
#         self.assertEqual(infix_to_postfix("A * B + C * D"), 'A B * C D * +' )
#         self.assertEqual(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"), 'A B + C * D E - F G + * -')
#
#     def test_postfix_eval(self):
#         self.assertEqual(postfix_eval('7 8 + 3 2 + /'), 3.0)
#
#     def test_calculator(self):
#         self.assertEqual(calculator("8 * ( 8 + 2 ) + 3"), 83)
#
#     def test_do_math(self):
#         self.assertEqual(do_math("*", 3, 4), 12)
#         self.assertEqual(do_math("/", 9, 3), 3)
#         self.assertEqual(do_math("+", 3, 4), 7)
#         self.assertEqual(do_math("-", 5, 3), 2)

def calculator(infix_expr):
    """
    Takes in an infix expression, evaluates it, and returns the result
    Supports the following mathematical functions: +, -, *, /, ^
    Logic -
        1) 'operator_stack' holds operators
        2) 'operand_stack' holds operands
        3) scan token list from left to right
            if token is:
                3a) an operand - convert from str --> int and push onto 'operand_stack'
                3b) '(' - push it onto 'operator_stack'
                3c) ')' - pop 'operator_stack' until corresponding left parenthesis is removed
                          for every operator popped from 'operator_stack', do 3d
                3d) an operator - pop 'operand_stack' twice, first pop is second operand,
                                  perform operation and push result back to stack
        4) pop operand_stack to return final value
    :param infix_expr: infix expression
    :return: evaluated result
    """

    # Assign precedence values to operators
    prec = {}
    prec['^'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    # Instantiate stacks
    operand_stack = Stack()
    operator_stack = Stack()

    try:
        token_list = infix_expr.split()
        logging.debug("token_list = {}".format(token_list))
    except:
        sys.exit(1)

    for token in token_list:
        logging.debug("token = {}".format(token))
        if token in '0123456789':
            operand_stack.push(int(token))
            logging.debug("operand_stack.push = {}".format(token))
        elif token == '(':
            operator_stack.push(token)
            logging.debug("operator_stack.push = {}".format(token))
        elif token == ')':
            logging.debug("token = {}".format(token))
            operator_token = operator_stack.pop()
            logging.debug("operator_stack.pop = {}".format(operator_token))
            while operator_token != '(':
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(operator_token, operand1, operand2)
                operand_stack.push(result)
                logging.debug("while operator_token != '(':\noperand1 = {} | operand2 = {} | token = {} | result = {}".format(
                    operand1, operand2, operator_token, result))
                operator_token = operator_stack.pop()
                logging.debug("new operator_token = {}".format(operator_token))
        elif token in '^*/+-':
            while (not operator_stack.isEmpty()) and \
                    (prec[operator_stack.peek()] >= prec[token]):
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                operator_token = operator_stack.pop()
                result = do_math(operator_token, operand1, operand2)
                operand_stack.push(result)
                logging.debug("Operator - While:\noperand1 = {} | operand2 = {} | token = {} | result = {}".format(
                    operand1, operand2, operator_token, result))
            operator_stack.push(token)
            logging.debug("operator_stack.push(): {}".format(token))
        else:
            logging.debug("else.... exiting....")
            sys.exit(1)

    # Use all remaining operators
    if not operator_stack.isEmpty():
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operator_token = operator_stack.pop()
        result = do_math(operator_token, operand1, operand2)
        logging.debug("Remaining Operators:\noperand1 = {} | operand2 = {} | token = {} | result = {}".format(
            operand1, operand2, operator_token, result))
        operand_stack.push(result)

    return operand_stack.pop()


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

    Error Checking:
    - Check if split() is successful
    - Reserve else in token checking for non valid characters
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

    try:
        token_list = infix_expr.split()
    except:
        sys.exit(1)


    for token in token_list:

        if not op_stack.isEmpty():
            logging.debug("token = {}, stack_peek = {}".format(token, op_stack.peek()))
        else:
            logging.debug("token = {}".format(token))

        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            operator_token = op_stack.pop()
            while operator_token != '(':
                postfix_list.append(operator_token)
                operator_token = op_stack.pop()
        elif token in '+-*/^':
            while (not op_stack.isEmpty()) and \
                    (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
        else:
            sys.exit(1)

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

    try:
        token_list = postfix_expr.split()
    except:
        sys.exit(1)

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        elif token in "*/+-^":
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
        else:
            sys.exit(1)
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
    if operator == "^":
        return op1**(op2)

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    # print(infix_to_postfix("5 * 3 ** ( 4 - 2 )"))
    print(calculator("8 * ( 8 + 2 ) + 3"))

if __name__ == '__main__':
    # unittest.main()
    main()