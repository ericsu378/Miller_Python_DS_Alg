__author__ = 'ESU'

####################################
# To-Do
# clean up variable names
# figure out why pyplot doesnt work w/in a function

####################################

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 2.3. Big-O Notation

# Self Check
# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list. O(n2).
# The second function should be linear O(n).

import time
from random import randrange
from matplotlib import pyplot

# 2 for loops means n*n
def min_n2(input_list):
    min = input_list[0]
    for i in input_list:
        is_smallest = True
        for j in input_list:
            if i > j:
                is_smallest = False
        if is_smallest:
            min = i
    return min

# Only go through list once
def min_n(input_list):
    min = input_list.pop()
    for i in input_list
        if i < min:
            min = i
    return min


# Timing code for proof
def test_time():
    listSize_list = []
    listSize_time = []
    for listSize in range(1000, 6001, 1000):
        input_list = [randrange(100000) for x in range(listSize)]
        start = time.time()
        print(min_n2(input_list))
        print(min_n(input_list))
        end = time.time()
        print("size; %d | time: %f" % (listSize, end-start))
        listSize_list.append(listSize)
        listSize_time.append(end-start)
    return (listSize_list, listSize_time)


def main():
    input_list = [3, 5, 7, 8, 1, 2, 3, 6, 7, 10]
    print(min_n(input_list))
    listSize_list, listSize_time = test_time()
    print(listSize_list)
    print(listSize_time)
    pyplot.plot(listSize_list, listSize_time)


if __name__ == '__main__':
    main()