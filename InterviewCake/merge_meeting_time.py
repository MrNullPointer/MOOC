def merge_ranges(meetings):
        #sort the meetings
    sorted_meetings = sorted(meetings)
        #the merged meetings list to be returned
    merged_meetings = [sorted_meetings[0]]

        #loop over the sorted_meetings
    for curr_start, curr_end in sorted_meetings[1:]:
            
            #get the previous values
        prev_start,prev_end = merged_meetings[-1]
            #check if the current meeting starts before the end of previous meeting
        if curr_start <= prev_end:
            merged_meetings[-1] = (prev_start, max(prev_end,curr_end))
        else:
            merged_meetings.append((curr_start, curr_end))
        
    return merged_meetings


meetings = [(0, 1), (3, 5), (4, 6), (10, 12), (9, 10)]
print(merge_ranges(meetings))
