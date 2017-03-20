# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# Self Check
#   Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem?
# The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will
# almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey
# with a Python function. How long do you think it would take for a Python function to generate just one sentence of
# Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”
#   You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate
# this is to write a function that generates a string that is 27 characters long by choosing random letters from the
# 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by
# comparing the randomly generated string to the goal.
#   A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s
# progress this third function should print out the best string generated so far and its score every 1000 tries.

# Self Check Challenge
#    See if you can improve upon the program in the self check by keeping letters that are correct and only modifying
# one character in the best string so far. This is a type of algorithm in the class of ‘hill climbing’ algorithms,
# that is we only keep the result if it is better than the previous one.

from difflib import SequenceMatcher
import string, random

# Generates a string that is 'size' characters long by choosing random letters from the 26 letters in the alphabet plus
# the space.
def generate_string(size):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(size))

# Scores each generated string by comparing the randomly generated string to the goal.
def score(test_str, gold_str):
    return SequenceMatcher(None, test_str, gold_str).ratio()

# Find location of first mis-match in string
def locate(test_str, gold_str):
    index = 0
    for char in test_str:
        if char != gold_str[index]:
            return index
        index += 1

# Repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.
# Print out the best string generated so far and its score every 1000 tries
def infinite_monkey(input):
    count = 0
    best = 0
    best_str = ''
    while True:
        count += 1
        test_str = generate_string(len(input))
        ratio = score(test_str, input)
        if ratio > best:
            best = ratio
            best_str = test_str
        if count % 1000 == 0:
            print("Count = {}, Current String = {}, Best String = {}, Ratio = {}".format(count, test_str, best_str, ratio))
        if ratio == 1.0:
            print("Count = {}, Best String = {}, Ratio = {}".format(count, best_str, ratio))
            print("Generated String matched the Gold String!!!\n")
            break

# Modification on infinite_monkey
# This version keeps letters that are correct and only modifies one character in the best string until the generated
# string is correct.
def infinite_monkey_challenge(input):
    print("Gold String = {}".format(input))
    gold_str = list(input)
    count = 0
    best = 0
    best_str = ''
    test_str = list(generate_string(len(gold_str)))
    while True:
        ratio = score(test_str, gold_str)
        if ratio > best:
            best = ratio
            best_str = test_str
        if ratio == 1.0:
            print("Count = {}, Best String = {}, Ratio = {}".format(count, ''.join(best_str), ratio))
            print("Generated String matched the Gold String!!!\n")
            break

        # If string doesn't match... cycle through test_str until all characters match
        idx = locate(test_str, gold_str)
        while test_str[idx] != gold_str[idx]:
            test_str[idx] = generate_string(1)
            count += 1
            if count % 100 == 0:
                print("Count = {}, Best String = {}, Ratio = {}".format(count, best_str, ratio))

def main():
    infinite_monkey_challenge('eric su')

if __name__ == '__main__':
    main()
