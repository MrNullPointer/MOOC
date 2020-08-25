from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, EmployeeID, intervalID):
        self.interval = interval
        self.employeeID = EmployeeID
        self.intervalID = intervalID

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):

    if schedule is None:
        return []

    result = []
    min_heap = []

    for idx in range(len(schedule)):
        heappush(min_heap, EmployeeInterval(schedule[idx][0], idx, 0))

    prev_interval = min_heap[0].interval

    while min_heap:
        heap_top = heappop(min_heap)

        if prev_interval.end < heap_top.interval.start:
            result.append(Interval(prev_interval.end, heap_top.interval.start))
            prev_interval = heap_top.interval
        else:
            if prev_interval.end < heap_top.interval.end:
                prev_interval = heap_top.interval

        employee_schedule = schedule[heap_top.employeeID]

        if len(employee_schedule) > heap_top.intervalID + 1:
            heappush(
                min_heap,
                EmployeeInterval(
                    schedule[heap_top.employeeID][heap_top.intervalID + 1],
                    heap_top.employeeID, heap_top.intervalID + 1))
    # TODO: Write your code here
    return result


def main():

    input = [[Interval(1, 3), Interval(5, 6)],
             [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)],
             [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)],
             [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
