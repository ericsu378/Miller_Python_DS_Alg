__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures Release 3.0
# Brad Miller, David Ranum
# September 22, 2013

# 1.4.5 Defining Functions Self Check

# The way we will simulate this is to write a function that generates a string that is 27 characters long by choosing
# random letters from the 26 letters in the alphabet plus the space.

# We will write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done.
# If the letters are not correct then we will generate a whole new string.
# To make it easier to follow your program's progress this third function should print out the best string generated
# so far and its score every 1000 tries.

# Self Check Challenge
# See if you can improve upon the program in the self check by keeping letters that are correct
# and only modifying one character in the best string so far. This is a type of algorithm in the
# class of 'hill climbing'' algorithms, that is we only keep the result if it is better than the previous
# one.

import random
import string

# Generate a random string
def generate_string(string_length = 27, chars =string.ascii_lowercase + " " ):
    # random.choice returns random element from sequence
    # Join a generator ( '(' instead of '[' )list comprehension with no spaces
    str = ''.join(random.choice(chars) for _ in range(string_length))
    return str

# Re-generate characters of a string only if it does not equal goal_string
def generate_string_v2(old_string, goal_string, chars =string.ascii_lowercase + " " ):
    # random.choice returns random element from sequence
    str = list(old_string)
    for i in range(len(old_string)):
        if old_string[i] != goal_string[i]:
            str[i] = random.choice(chars)
    str = "".join(str)
    return str

def score(generated_string, goal_string):
    count = 0.0
    str_length = len(generated_string)
    for i in range(str_length):
        if generated_string[i] == goal_string[i]:
            count += 1
    if count != 0:
        score_percentage = count/str_length
    else:
        score_percentage = 0.0
    return score_percentage

def run_generator(mode=1):
    count = 0
    done = False
    goal_string = "methinks it is like a weasel"
    # goal_string = "aaaaaaaaaaaaaaaaaa"
    best_string = ""
    best_score = 0.0
    print "Goal String = " + str(goal_string)
    if mode == 1:
        while done != True:
            count +=1
            test_string = generate_string(string_length = len(goal_string))
            current_score = score(test_string, goal_string)
            if current_score > best_score:
                best_string = test_string
                best_score = current_score
            if current_score == 1.0:
                done = True
            if count % 1000 == 0:
                print "Count = " + str(count)
                print "Best String = " + str(best_string)
                print "Best Score = " + str(best_score)
    if mode == 2:
        best_string = generate_string(string_length = len(goal_string))
        best_score = score(best_string, goal_string)
        while done != True:
            count +=1
            test_string = generate_string_v2(best_string, goal_string)
            current_score = score(test_string, goal_string)
            if current_score > best_score:
                best_string = test_string
                best_score = current_score
                print "Count = " + str(count)
                print "Best String = " + str(best_string)
                print "Best Score = " + str(best_score)
            if current_score == 1.0:
                done = True
            if count % 1000 == 0:
                print "Count = " + str(count)
                print "Best String = " + str(best_string)
                print "Best Score = " + str(best_score)

run_generator(mode=2)