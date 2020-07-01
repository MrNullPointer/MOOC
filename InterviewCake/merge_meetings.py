def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    
    for idx in range(1,len(sorted_meetings)):
        if idx >= len(sorted_meetings):
            return sorted_meetings
        curr_start, curr_end = sorted_meetings[idx]
        prev_start, prev_end = sorted_meetings[idx - 1]

        if prev_end >= curr_start:
            sorted_meetings[idx - 1] = (prev_start, max(prev_end, curr_end))
            sorted_meetings.pop(idx)
    return sorted_meetings

meetings = [(0, 1), (3, 5), (4, 6), (10, 12), (9, 10)]
print(merge_ranges(meetings))

meetings = [(5, 6), (6, 8)]
print(merge_ranges(meetings))


meetings = [(1, 4), (2, 5), (5, 8)]
print(merge_ranges(meetings))
