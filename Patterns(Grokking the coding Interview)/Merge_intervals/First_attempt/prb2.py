from heapq import *


class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end

def find_max_cpu_load(jobs):
    # TODO: Write your code here
    max_cpu_load, curr_cpu_load = 0, 0
    min_head = []
    jobs.sort(key = lambda x : x.start)

    for job in jobs:
        while len(min_head) > 0 and min_head[0].end <= job.start:
            curr_cpu_load -= min_head[0].cpu_load
            heappop(min_head)
        
        heappush(min_head, job)
        curr_cpu_load += job.cpu_load

        max_cpu_load = max(max_cpu_load, curr_cpu_load)

    return max_cpu_load




def main():
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(
              1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(6, 7, 10),
                                 job(2, 4, 11),
                                 job(8, 12, 15)])))
    print("Maximum CPU load at any time: " +
          str(find_max_cpu_load([job(
              1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
