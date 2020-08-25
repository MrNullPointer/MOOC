from heapq import *


class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings):
    # TODO: Write your code here
    meetings.sort(key=lambda x: x.start)

    rooms = 0
    minheap = []

    for meeting in meetings:
        if len(minheap) > 0 and meeting.start >= minheap[0].end:
            heappop(minheap)

        heappush(minheap, meeting)
        rooms = max(len(minheap), rooms)
    return rooms


def main():
    print("Minimum meeting rooms required: " + str(
        min_meeting_rooms(
            [Meeting(4, 5),
             Meeting(2, 3),
             Meeting(2, 4),
             Meeting(3, 5)])))
    print(
        "Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(
            1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print(
        "Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(
            6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print(
        "Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(
            1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(
        min_meeting_rooms(
            [Meeting(4, 5),
             Meeting(2, 3),
             Meeting(2, 4),
             Meeting(3, 5)])))


main()