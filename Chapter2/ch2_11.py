__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 3.10. Discussion Questions
# Give the Big-O performance of the following code fragments:
#
# 1) Big-O = n^2
# for i in range(n):
#    for j in range(n):
#       k = 2 + 2
#
# 2) Big-O = n
# for i in range(n):
#      k = 2 + 2
#
# 3) Big-O = log(n)
# i = n
# while i > 0:
#    k = 2 + 2
#    i = i // 2
#
# 4) Big-O = n^3
# for i in range(n):
#    for j in range(n):
#       for k in range(n):
#          k = 2 + 2
#
# 5) Big-O = log(n)
# i = n
# while i > 0:
#    k = 2 + 2
#    i = i // 2
#
# 6) Big-O = n
# for i in range(n):
#    k = 2 + 2
# for j in range(n):
#    k = 2 + 2
# for k in range(n):
#    k = 2 + 2

# 3.11. Programming Exercises
# 1) Devise an experiment to verify that the list index operator is O(1)
#    According to notes and https://wiki.python.org/moin/TimeComplexity, list index operator should be O(1)
#    Yet some argue, along with test results, that the complexity of list index operator is actually O(n)
#    list.index(x) Returns the index in the list of the first item whose value is x. Which may imply searching
#    which means you're effectively doing 'x in s' which is O(n).
#    https://stackoverflow.com/questions/5913671/complexity-of-list-indexx-in-python
# 2) Devise an experiment to verify that get item and set item are O(1) for dictionaries.
# 3) Devise an experiment that compares the performance of the 'del' operator on lists and dictionaries.
# 4) Given a list of numbers in random order, write an algorithm that works in O(nlog(n))
#    to find the kth smallest number in the list.
#    Answer: Sort array and return 'k'th element. Python sort is O(nlogn), returning element is O(1)
# 5) Can you improve the algorithm from the previous problem to be linear? Explain.
#    http://www.codinghelmet.com/?path=exercises/kth-smallest

# Dict Del 100000 elements | TimeIt Time = 0.000002228 seconds
# List Del 100000 elements | TimeIt Time = 0.000192369 seconds
# Dict Del 200000 elements | TimeIt Time = 0.000002810 seconds
# List Del 200000 elements | TimeIt Time = 0.000417221 seconds
# Dict Del 300000 elements | TimeIt Time = 0.000002333 seconds
# List Del 300000 elements | TimeIt Time = 0.000625320 seconds
# Dict Del 400000 elements | TimeIt Time = 0.000002436 seconds
# List Del 400000 elements | TimeIt Time = 0.000826238 seconds
# Dict Del 500000 elements | TimeIt Time = 0.000002561 seconds
# List Del 500000 elements | TimeIt Time = 0.001181484 seconds
# Dict Del 600000 elements | TimeIt Time = 0.000002778 seconds
# List Del 600000 elements | TimeIt Time = 0.007659391 seconds
# Dict Del 700000 elements | TimeIt Time = 0.000003010 seconds
# List Del 700000 elements | TimeIt Time = 0.017433413 seconds
# Dict Del 800000 elements | TimeIt Time = 0.000002931 seconds
# List Del 800000 elements | TimeIt Time = 0.002271172 seconds
# Dict Del 900000 elements | TimeIt Time = 0.000002856 seconds
# List Del 900000 elements | TimeIt Time = 0.003127566 seconds
# Dict Del 1000000 elements | TimeIt Time = 0.000003210 seconds

# Experiment Notes:
# We want to benchmark operations against different size datasets in order to characterize its complexity.
# We will do this through
#   1) Isolating each test within its own function and wrapping it within a timeit object to ensure we are testing
#      in isolation
#   2) For each function, we will cycle through 'x' different element sizes in order to show the operations
#      characterization over different data structure sizes

import timeit
import random
import matplotlib.pyplot as plt
import unittest

class TestExamples(unittest.TestCase):

    def test_count_elements(self):
        self.test_list = [1, 5, 9, 4, 2, 3, 6, 8, 7, 0]
        self.assertEqual(count_elements(self.test_list, len(self.test_list), 6), (6,3))

    def test_find_pivot(self):
        self.test_list = [1, 5, 9, 4, 2, 3, 6, 8, 7, 0]
        self.assertEqual(find_pivot(self.test_list, len(self.test_list), 5), 6)


# 1
def verify_list_idx(test_list, retrieve_count):
    for i in range(retrieve_count):
        # idx = random.randint(0, len(test_list)-1)
        idx = 100
        test_list[idx]
        # test_list.index(idx) # O(n) since it returns first item, so its doing a search.

# 2
test_dictionary = {}

def verify_dict_set(get_set_count):
    global test_dictionary
    for i in range(get_set_count):
        test_dictionary[i] = i

def verify_dict_get(get_set_count):
    global test_dictionary
    for i in range(get_set_count):
        x = test_dictionary[i]

# 3
def verify_dict_del(test_dict, element_count):
    for i in range(element_count):
        del test_dict[i]

def verify_list_del(test_list, element_count):
    for i in range(element_count):
        test_list.remove(i)

# 4
def find_kth_smallest_nlogn(input_list, k):
    input_list.sort()
    return input_list[k+1]

# 5 #
# Modified QuickSort
# Find Pivot point using median of medians, then do QuickSort
# Inspiration provided by: http://www.codinghelmet.com/?path=exercises/kth-smallest
def find_kth_smallest_n(input_list, k):
    n = len(input_list)
    c = 5
    print('input_list = {}'.format(input_list))
    print('n = {}, c = {}'.format(n, c))

    while(True):
        # Find pivot point using median of medians
        pivot = find_pivot(input_list, n, c)
        # break

        # Count number of elements smaller and larger than pivot point
        smaller_count, larger_count = count_elements(input_list, n, pivot)
        print('input_list = {}'.format(input_list))
        print('k = {} | n = {} | pivot = {} | smaller_count = {} | larger_count = {}'.format(k, n, pivot, smaller_count, larger_count))
        # Partition array
        if (k < smaller_count):
            if_loop = 'k < smaller_count'
            n = partition(input_list, n, pivot, True)
        elif (k < (n - larger_count)):
            return_value =  pivot
            break
        else:
            if_loop = 'else'
            k = k - (n - larger_count)
            n = partition(input_list, n, pivot, False)
        print('if_loop = {} | n = {}'.format(if_loop, n))

    return return_value

def find_pivot(input_list, n, c):
    """
    Use median of medians to return optimal pivot point
    Will reduce the array and repeat recursively until last median of medians
    :param input_list: list array
    :param n: list array length
    :param c: column size
    :return: pivot location
    """
    while (n > 1):
        pos = 0
        print('Start find_pivot -- n = {}'.format(n))
        print('input_list')
        print(input_list)
        for start in range(0, n, c):
            end = start + c
            # if last column has less than c elements, set end to n
            if (end > n):
                end = n

            # Sort Column... could use python's built-in sort?
            for i in range(start, (end - 1), 1):
                for j in range((i + 1), end, 1):
                    print('Pivot - sort: | i = {} | j = {}'.format(i, j))
                    if (input_list[j] < input_list[i]):
                        tmp = input_list[i]
                        input_list[i] = input_list[j]
                        input_list[j] = tmp
                        print('input_list = {}'.format(input_list))

            # Find column's median and promote to beginning of array
            # ? why swap? conserve memory?
            median = (start + end) // 2 # Median position
            tmp = input_list[median]
            input_list[median] = input_list[pos]
            input_list[pos] = tmp
            pos = pos + 1
            print('start = {} | end = {} | pos = {}'.format(start, end, pos))
            print('input_list = {}'.format(input_list))
        n = pos # reduce the array and repeat recursively

    print('Exit! | n = {} | pivot value = {}'.format(n, input_list[0]))
    return input_list[0] # last median of medians is the pivot


def partition(input_list, n, pivot, extractSmaller):
    """
    Go through input_list, and if value is less than pivot value, swap to front
    ??? how do edits on 'input_list' within method affect 'input_list' outside of method?
    :param input_list:
    :param n:
    :param pivot:
    :param extractSmaller:
    :return: return_value, kth element
    """
    pos = 0
    for i in range(0, n, 1):
        if ((extractSmaller and input_list[i] < pivot) or (not extractSmaller and input_list[i] > pivot)):
            tmp = input_list[i]
            input_list[i] = input_list[pos]
            input_list[pos] = tmp
            pos = pos + 1
            print('i = {} | pos = {} | input_list = {}'.format(i, pos, input_list))
    n = pos
    return n

def count_elements(input_list, n, pivot):
    """
    Counts number of smaller and larger elements wrt to pivot point
    :param input_list:
    :param n:
    :param pivot:
    :return: (smaller_count, larger_count)
    """
    smallerCount = 0
    largerCount = 0
    for i in range(n):
        if input_list[i] < pivot:
            smallerCount += 1
        elif input_list[i] > pivot:
            largerCount += 1
    return smallerCount, largerCount


def main():
    # # 1
    # lst_size_array = []
    # lst_timeit_time = []
    # retrieve_count = 10
    #
    # for lst_size in range(100000, 1000001, 100000):
    #     test_list = list(range(lst_size))
    #     idxTime = timeit.Timer("verify_list_idx("+str(test_list)+","+str(retrieve_count)+")",
    #                            "from __main__ import verify_list_idx")
    #     t1 = idxTime.timeit(number=100)
    #     print("List Size = %d | Pulled %d elements | TimeIt Time = %10.9f seconds" % (lst_size, retrieve_count, t1))
    #     lst_size_array.append(lst_size)
    #     lst_timeit_time.append(t1)
    # plt.figure(1)
    # plt.plot(lst_size_array, lst_timeit_time)
    # plt.title("Verify List Index Operator")
    # plt.xlabel("List Size")
    # plt.ylabel("Time(Seconds)")
    # plt.show()

    # # 2
    # dict_get_set_count = []
    # dict_set_timeit_time = []
    # dict_get_timeit_time = []
    #
    # for get_set_count in range(100000, 1000001, 100000):
    #     set_time_obj = timeit.Timer("verify_dict_set("+str(get_set_count)+")",
    #                            "from __main__ import verify_dict_set")
    #     t2 = set_time_obj.timeit(number=300)
    #     t2 = t2 / get_set_count # for normalization
    #     print("Set %d elements | TimeIt Time = %10.9f seconds" % (get_set_count, t2))
    #     dict_get_set_count.append(get_set_count)
    #     dict_set_timeit_time.append(t2)
    #
    # for get_set_count in range(100000, 1000001, 100000):
    #     get_time_obj = timeit.Timer("verify_dict_get("+str(get_set_count)+")",
    #                            "from __main__ import verify_dict_get")
    #     t3 = get_time_obj.timeit(number=300)
    #     t3 = t3 / get_set_count # for normalization
    #     print("Set %d elements | TimeIt Time = %10.9f seconds" % (get_set_count, t3))
    #     dict_get_timeit_time.append(t3)
    #
    # plt.figure(2)
    # plt.plot(dict_get_set_count, dict_set_timeit_time, marker = 'o', label = "Dict Set")
    # plt.plot(dict_get_set_count, dict_get_timeit_time, marker = '*', label = "Dict Get")
    # plt.title("Verify Dict Get/Set Operator")
    # plt.xlabel("Get/Set Element Count")
    # plt.ylabel("Time(Seconds)")
    # plt.legend()
    # plt.show()

    # # 3
    # element_count_list = []
    # dict_del_timeit_time = []
    # list_del_timeit_time = []
    # for element_count in range(100000, 1000001, 100000):
    #     test_del_dict = {i : i for i in range(element_count)}
    #     dict_del_time_obj = timeit.Timer("verify_dict_del("+str(test_del_dict)+","+str(element_count)+")",
    #                            "from __main__ import verify_dict_del")
    #     t4 = dict_del_time_obj.timeit(number=10) / element_count
    #     print("Dict Del %d elements | TimeIt Time = %10.9f seconds" % (element_count, t4))
    #
    #
    #     test_del_list = [i for i in range(element_count)]
    #     list_del_time_obj = timeit.Timer("verify_list_del("+str(test_del_list)+","+str(element_count)+")",
    #                            "from __main__ import verify_list_del")
    #     t5 = list_del_time_obj.timeit(number=10) / element_count
    #     print("List Del %d elements | TimeIt Time = %10.9f seconds" % (element_count, t5))
    #
    #     element_count_list.append(element_count)
    #     dict_del_timeit_time.append(t4)
    #     list_del_timeit_time.append(t5)
    #
    # plt.figure(3)
    # plt.plot(element_count_list, dict_del_timeit_time, marker = 'o', label = "Dict Del")
    # plt.plot(element_count_list, list_del_timeit_time, marker = '*', label = "List Del")
    # plt.title("Verify Dict/List Del Operator")
    # plt.xlabel("Dict/List Element Count")
    # plt.ylabel("Time(Seconds)")
    # plt.legend()
    # plt.show()
    #
    # # 4
    # test_sort_list = [random.randint(0,1000) for i in range(20)]
    # print(test_sort_list)
    # print(find_kth_smallest_nlogn(test_sort_list, 1))

    # 5
    input_list = [1, 5, 9, 4, 2, 3, 6, 8, 7, 0]
    x = find_kth_smallest_n(input_list, 3)
    print(x)

if __name__ == '__main__':
    # unittest.main()
    main()