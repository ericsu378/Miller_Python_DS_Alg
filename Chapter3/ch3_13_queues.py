__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures
# Brad Miller, David Ranum
# http://interactivepython.org/runestone/static/pythonds/index.html

# How would you modify the printer simulation to reflect a larger number of students? Suppose that the number of
# students was doubled. You make need to make some reasonable assumptions about how this simulation was put together
# but what would you change? Modify the code. Also suppose that the length of the average print task was cut in half.
# Change the code to reflect that change. Finally How would you parametertize the number of students, rather than
# changing the code we would like to make the number of students a parameter of the simulation.

# Answer: printer_sim has been modified to take in number of students and the number of pages a student prints per job.
#         Default values are 10 students with 2 jobs per hour
#         To double, just change 10 to 20 students
#         Length of the average print task is easily changed by changing the pages per minute value (ppm) of the printer

# 3.27 Programming Exercises:
# 6) Design and implement an experiment to do benchmark comparisons of the two queue implementations.
# What can you learn from such an experiment?
# Experiment:
# The only difference between 'Queue' and 'Queue_v2' are the dequeue and enqueue functions. With this known,
# our experiment will test 3 cases:
#   1) # Enqueues >> # Dequeues
#   2) # Enqueues == # Dequeues
#   3) # Enqueues << # Dequeues

from ch3_DataStructures import Queue, Queue_v2, Queue_linked_list
import unittest
import random
import timeit
import sys

# class TestExamples(unittest.TestCase):
#
#     def test_hot_potato(self):
#         queue = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
#         count = 7
#         self.assertEqual(hot_potato(queue, count), 'Susan')


def hot_potato(namelist, num):
    """
    General simulation of hot potato
    :param namelist: list of names
    :param num: constant used for counting
    :return: return name of last person remaining after repetitive counting by num
    """

    sim_queue = Queue()

    # Create Name Queue
    for name in namelist:
        sim_queue.enqueue(name)
    print("Queue: {}\nRemoving person after {} turns".format(sim_queue.return_obj(), num))

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        print("Removed: {} | Queue: {}".format(sim_queue.dequeue(), sim_queue.return_obj()))

    return sim_queue.dequeue()


class Printer:
    """
    Emulates printer
     - task, if its busy, and amount of time needed and timer
    """
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * (60/self.page_rate)

class Task():
    """
    Emulates a task
    - a task will be between 1 to 20 pages and have a timestamp to compute wait time
    """
    def __init__(self, time, print_tasks_per_hour):
        self.timestamp = time
        self.pages = random.randrange(1, (print_tasks_per_hour + 1))

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return (current_time - self.timestamp)

def printer_sim(run_time, ppm, num_students, pages_printed):

    lab_printer = Printer(ppm)
    print_queue = Queue()
    waiting_times = []
    print_tasks_per_hour = (num_students * pages_printed)

    for current_second in range(run_time):

        if new_print_task(num_students, pages_printed):
            task = Task(current_second, print_tasks_per_hour)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    avg_wait_time = sum(waiting_times)/len(waiting_times)
    print("Average Wait: {0:6.2f} secs || {1:3d} tasks remaining.".format(avg_wait_time, print_queue.size()))

def new_print_task(num_students, pages_printed):
    """
    Helper function
    10 students / hr who print up to 2x /hr.
        ~ 20 print tasks / hr = 1 print task / 180 secs
            simulate with 1/180 probability
    :return: True or False
    """
    print_probability = 3600 / (num_students * pages_printed)
    num = random.randrange(1, (print_probability + 1))
    if num == print_probability:
        return True
    else:
        return False


# 3.27 Programming Exercises:
# 6) Design and implement an experiment to do benchmark comparisons of the two queue implementations.
# What can you learn from such an experiment?
# Experiment:
# The only difference between 'Queue' and 'Queue_v2' are the dequeue and enqueue functions. With this known,
# our experiment will test 3 cases:
#   1) # Enqueues >> # Dequeues
#   2) # Enqueues == # Dequeues
#   3) # Enqueues << # Dequeues
# * Due to the limitations of timeit module, we need to embed the queue priming function within the timeit function call.
#   Without this, the timeit function will just re-use the same queue object (without re-priming) for each iteration
#
# Queue is quicker to dequeue, while Queue_v2 is quicker to enqueue. This is because queue's dequeue is O(1) and queue_v2's
# enqueue is O(1).
# Results line up for the queue_v2 case, yet queue takes longer to dequeue than queue_v2...?
# Queue | Queue_init_count = 5000 | num_enqueue = 10 | num_dequeue = 2500 | avg_time = 0.005969544381327411
# Queue | Queue_init_count = 5000 | num_enqueue = 1000 | num_dequeue = 1000 | avg_time = 0.008848330458783317
# Queue | Queue_init_count = 5000 | num_enqueue = 2500 | num_dequeue = 10 | avg_time = 0.014655742307460388
# Queue_v2 | Queue_init_count = 5000 | num_enqueue = 10 | num_dequeue = 2500 | avg_time = 0.0033260769298864967
# Queue_v2 | Queue_init_count = 5000 | num_enqueue = 1000 | num_dequeue = 1000 | avg_time = 0.0024393638513182684
# Queue_v2 | Queue_init_count = 5000 | num_enqueue = 2500 | num_dequeue = 10 | avg_time = 0.0008621788689996417

def prime_queue(queue_init_count):
    """
    helper function to prime initial queue
    :param queue_init_count:
    :return: queue object primed
    """
    queue_obj = Queue()
    for i in range(queue_init_count):
        queue_obj.enqueue(i)
    return queue_obj

def prime_queue_v2(queue_init_count):
    """
    helper function to prime initial queue
    :param queue_init_count:
    :return: queue object primed
    """
    queue_v2_obj = Queue_v2()
    for i in range(queue_init_count):
        queue_v2_obj.enqueue(i)
    return queue_v2_obj

def prime_queue_linked_list(queue_init_count):
    """
    helper function to prime initial queue
    :param queue_init_count:
    :return: queue object primed
    """
    queue_linked_list_obj = Queue_linked_list()
    for i in range(queue_init_count):
        queue_linked_list_obj.enqueue(i)
    return queue_linked_list_obj

def benchmark_prime_queue(iterations):
    """
    Benchmark to get average time of priming queue
    :param iterations: number parameter in timeit
    :return: average time
    """
    queue_init_count = 1000
    timeit_obj = timeit.Timer("prime_queue("+str(queue_init_count)+")",
                           "from __main__ import prime_queue")
    total_time = timeit_obj.timeit(number=iterations)
    return (total_time/queue_init_count)/iterations

def benchmark_prime_queue_v2(iterations):
    """
    Benchmark to get average time of priming queue
    :param iterations: number parameter in timeit
    :return: average time
    """
    queue_init_count = 1000
    timeit_obj = timeit.Timer("prime_queue_v2("+str(queue_init_count)+")",
                           "from __main__ import prime_queue_v2")
    total_time = timeit_obj.timeit(number=iterations)
    return (total_time/queue_init_count)/iterations

def benchmark_prime_queue_linked_list(iterations):
    """
    Benchmark to get average time of priming queue
    :param iterations: number parameter in timeit
    :return: average time
    """
    queue_init_count = 1000
    timeit_obj = timeit.Timer("prime_queue_linked_list("+str(queue_init_count)+")",
                           "from __main__ import prime_queue_linked_list")
    total_time = timeit_obj.timeit(number=iterations)
    return (total_time/queue_init_count)/iterations

def benchmark_queue(option, queue_init_count, num_enqueue, num_dequeue):
    """
    Benchmark function to perform different numbers of enqueues and dequeues
    :param option: 1 = queue, 2 = queue_v2, 3 = queue_linked_list
    :param queue_init_count: number of elements to initialize initial queue to
    :param num_enqueue: number of times to enqueue
    :param num_dequeue: number of times to dequeue
    :return: None (timing done by timeit outside of function
    """
    if option == 1:
        queue_obj = prime_queue(queue_init_count)  # adds roughly 6.7e-07 sec
    elif option == 2:
        queue_obj = prime_queue_v2(queue_init_count) # adds roughly 3.1e-07 secs
    elif option == 3:
        queue_obj = prime_queue_linked_list(queue_init_count)
    else:
        sys.exit(1)
    for i in range(num_enqueue):
        queue_obj.enqueue(i)
    for i in range(num_dequeue):
        queue_obj.dequeue()

def benchmark_queue_test():
    iterations = 500
    queue_init_count = 5000
    enqueue_dequeue = [(10, 2500), (1000, 1000), (2500, 10)]
    queue_option = 1
    queue_v2_option = 2
    queue_linked_list_option = 3
    queue_prime_time = benchmark_prime_queue(4000)
    queue_v2_prime_time = benchmark_prime_queue_v2(4000)
    queue_linked_list_prime_time = benchmark_prime_queue_linked_list(4000)

    # Queue
    for (num_enqueue, num_dequeue) in (enqueue_dequeue):
        timeit_obj = timeit.Timer("benchmark_queue("+str(queue_option)+","+str(queue_init_count)+","+str(num_enqueue)
        +","+str(num_dequeue)+")", "from __main__ import benchmark_queue")
        total_time = timeit_obj.timeit(number=iterations)
        print("Queue | Queue_init_count = {} | num_enqueue = {} | num_dequeue = {} | avg_time = {}".format(
            queue_init_count, num_enqueue, num_dequeue, ((total_time/iterations) - (queue_prime_time * queue_init_count))
        ))

    # Queue_v2
    for (num_enqueue, num_dequeue) in enqueue_dequeue:
        timeit_obj = timeit.Timer("benchmark_queue("+str(queue_v2_option)+","+str(queue_init_count)+","+str(num_enqueue)
        +","+str(num_dequeue)+")", "from __main__ import benchmark_queue")
        total_time = timeit_obj.timeit(number=iterations)
        print("Queue_v2 | Queue_init_count = {} | num_enqueue = {} | num_dequeue = {} | avg_time = {}".format(
            queue_init_count, num_enqueue, num_dequeue, ((total_time/iterations) - (queue_v2_prime_time * queue_init_count))
        ))

    # Queue_linked_list
    for (num_enqueue, num_dequeue) in enqueue_dequeue:
        timeit_obj = timeit.Timer(
            "benchmark_queue(" + str(queue_linked_list_option) + "," + str(queue_init_count) + "," + str(num_enqueue)
            + "," + str(num_dequeue) + ")", "from __main__ import benchmark_queue")
        total_time = timeit_obj.timeit(number=iterations)
        print("Queue_linked_list | Queue_init_count = {} | num_enqueue = {} | num_dequeue = {} | avg_time = {}".format(
            queue_init_count, num_enqueue, num_dequeue,
            ((total_time / iterations) - (queue_linked_list_prime_time * queue_init_count))
        ))

def main():

    # # Hot Potato
    # queue = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    # count = 7
    # print("Last person standing: {}".format(hot_potato(queue, count)))
    #
    # # Printer Sim
    # for i in range(10):
    #     printer_sim(3600, 5, 10, 2)

    # print(benchmark_prime_queue(4000)/4000) # returns avg time it takes to prime 1 queue obj
    # print(benchmark_prime_queue_v2(4000)/4000) # returns avg time it takes to prime 1 queue

    benchmark_queue_test()


if __name__ == '__main__':
    main()
    # unittest.main()
