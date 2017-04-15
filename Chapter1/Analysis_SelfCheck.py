__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# Self Check
# Write two Python functions to find the minimum number in a list.
# The first function should compare each number to every other number on the list O(n2).
# The second function should be linear O(n).

import copy
import time
import timeit
import random
import matplotlib.pyplot as plt

# Find local minimum, compare with global minimum
def findMin_n2(list):
    # # Old (deepcopy takes awhile)
    # # to keep the original list intact, create two new lists with deepcopy so 'pop' won't affect original list
    # list1 = copy.deepcopy(list)
    # list2 = copy.deepcopy(list)
    # minimum = list1.pop(0)
    # for num1 in list1:
    #     for num2 in list2:
    #         # local minimum
    #         if num1 < num2:
    #             # global minimum
    #             if num1 < minimum:
    #                 minimum = num1
    # return minimum

    # Miller
    overallmin = list[0]
    for i in list:
        issmallest = True
        for j in list:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin

def findMin_n(list):
    # Old (deepcopy takes awhile)
    # # to keep the original list intact, create new list with deepcopy so 'pop' won't affect original list
    # list1 = copy.deepcopy(list) # could also use minimum = list[0]
    # minimum = list1.pop(0) # initializes minimum number with first item in list and removes from list
    # for num in list1:
    #     if num < minimum:
    #         minimum = num
    # return minimum

    # Miller
    minimum = list[0] # instantiate
    for num in list:
        if num < minimum:
            minimum = num
    return minimum

def multipleRuns(list_start, list_end, list_stepsize, funcType):
    listSize_list = []
    time_list = []
    for listSize in range(list_start, list_end, list_stepsize):
        alist = [random.randrange(100000) for x in range(listSize)]
        start = time.time()
        if funcType == 'n':
            print(findMin_n(alist))
        if funcType == 'n2':
            print(findMin_n2(alist))
        end = time.time()
        print("size = %d  time = %f" % (listSize, end-start))
        listSize_list.append(listSize)
        time_list.append(end-start)
    plt.figure()
    plt.plot(listSize_list, time_list)
    plt.ylabel('Time')
    plt.xlabel('List Size')
    plt.title(funcType)
    plt.show()

# Programming Exercises
# Devise an experiment to verify that the list index operator is O(1)
# Have lists of different sizes, retrieve a random element within list, measure time
def list_o1():
    n = random.randrange(1000) + 1
    alist = [random.randrange(100000) for x in range(n)]
    return alist[random.randrange(n)]

def time_list():
    t1 = timeit.Timer("list_o1()", "from __main__ import list_o1")
    for i in range(10):
        print("concat ", t1.timeit(number=100), "milliseconds")


# Devise an experiment to verify that get item and set item are O(1) for dictionaries.
# Create random dictionary sizes, test get and set
def dict_get_o1():
    n = random.randrange(1000) + 1
    x = {j:None for j in range(n)}
    return x.get(random.randrange(n))

def dict_set_o1():
    n = random.randrange(1000) + 1
    x = {j:None for j in range(n)}
    x[random.randrange(n)]="junk"

def time_dict():
    t2 = timeit.Timer("dict_get_o1()", "from __main__ import dict_get_o1")
    t3 = timeit.Timer("dict_set_o1()", "from __main__ import dict_set_o1")
    for i in range(10):
        print("concat ", t2.timeit(number=100), "milliseconds")
        print("concat ", t3.timeit(number=100), "milliseconds")


# Devise an experiment that compares the performance of the del operator on lists and dictionaries.
def list_del():
    n = random.randrange(1000) + 1
    alist = [random.randrange(100000) for x in range(n)]
    del alist[random.randrange(n)]

def dict_del():
    n = random.randrange(1000) + 1
    x = {j:None for j in range(n)}
    del x[random.randrange(n)]

def time_del():
    t4 = timeit.Timer("list_del()", "from __main__ import list_del")
    t5 = timeit.Timer("dict_del()", "from __main__ import dict_del")
    for i in range(10):
        print("Del_List: %f | Del_Dict: %f"%(t4.timeit(number=100), t5.timeit(number=100)))


# Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
# Sort is nlogn, n is stepping through each item, the sorting is logn
def get_kth_number(alist, k):
    alist.sort()
    return alist[k-1]

# Can you improve the algorithm from the previous problem to be linear? Explain.
# Resources:
# https://stackoverflow.com/questions/12546760/complexity-of-finding-k-th-largest-element-using-median-of-medians
# http://www.ardendertat.com/2011/10/27/programming-interview-questions-10-kth-largest-element-in-array/
# https://stackoverflow.com/questions/33100868/find-largest-k-th-element-through-median-of-medians-and-partition-around-k
# def partition(a, p, r, pivot):
#     """
#     Permutes the elements of a[p..r] (inclusive) in-place:
#        first elements <= a[r], then a[r], then those > a[r].
#     Returns the new location (index) of pivot value a[r] in the array.
#     """
#     i = p - 1
#     for j in range(p, r + 1):
#         if a[j] < pivot:
#             i = i + 1
#             a[i], a[j] = a[j], a[i]
#
#     return i
#
# def mom(a, left, right):
#     """
#     Returns the median of medians for array a.
#     """
#     length = right - left + 1
#     if length <= 0:
#         return
#     if length <= 5:
#         return sorted(a[left : right + 1])[length/2]
#
#     num_of_medians = length/5
#     medians = [mom(a, left + 5*i, left + 5 * (i + 1) - 1) for i in range(num_of_medians)]
#     return mom(medians, 0, len(medians) - 1)
#
# def kth(a, left, right, k):
#     """
#     ~~~~~
#     NOTE: k here means k-th smallest element. So in an array of length 10, the
#     k-th smallest element is the (len(array) - k)-th largest element.
#     ~~~~~
#
#     Partitions the array a around the median of medians pivot. Keeps finding new
#     pivots until the pivot == k. Then the partition is around k.
#     then a[(len(a) - k)...(len(a)-1)] will output the largest k elements (not sorted)
#     """
#     pivotIndex = mom(a, left, right)
#
#     pivotIndex = partition(a, left, right, pivotIndex)
#
#     while k != pivotIndex + 1:
#
#         if k > pivotIndex + 1:
#             pivotIndex = kth(a, pivotIndex + 1, right, k)
#
#         elif k < pivotIndex + 1:
#             pivotIndex = kth(a, left, pivotIndex, k)
#
#     return pivotIndex #this is index of the kth largest element
#
#
# def get_kth_number(alist, kth):
#     imax = 0
#     if kth > (len(alist) / 2):
#         imax = len(alist) - kth + 1
#     idx = 0
#     if imax == 0:
#         cur = alist[idx]
#         while idx < kth:
#     else:
#     return kth, imax\n",
#
#       "sample_list = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]\n",
#       "print(get_kth_number(sample_list, 7))"
#        "output_type": "stream",
#        "stream": "stdout",
#        "text": [
#         "(7, 5)\n"
#      "prompt_number": 15





def main():
    # testList = range(3, 50)
    # print testList
    # print findMin_n2(testList)
    # print findMin_n(testList)
    # multipleRuns(1000, 10001, 1000, 'n')
    # multipleRuns(1000, 10001, 1000, 'n2')
    # time_list()
    # time_dict()
    time_del()


if __name__ == '__main__': main()

