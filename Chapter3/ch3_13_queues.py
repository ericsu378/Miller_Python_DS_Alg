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


from ch3_DataStructures import Queue
import unittest
import random

class TestExamples(unittest.TestCase):

    def test_hot_potato(self):
        queue = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
        count = 7
        self.assertEqual(hot_potato(queue, count), 'Susan')


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


def main():

    # Hot Potato
    queue = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    count = 7
    print("Last person standing: {}".format(hot_potato(queue, count)))


    # Printer Sim
    for i in range(10):
        printer_sim(3600, 5, 10, 2)

if __name__ == '__main__':
    # unittest.main()
    main()