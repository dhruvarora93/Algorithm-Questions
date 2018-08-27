def merge_meeting_times(meetings):
    sorted_meetings = sorted(meetings, key=lambda x: x[0])
    condensed_list = [sorted_meetings[0]]
    for meeting in sorted_meetings[1:]:
        if meeting[0] <= condensed_list[-1][1]:
            condensed_list[-1] = (condensed_list[-1][0],max(condensed_list[-1][1],meeting[1]))
        else:
            condensed_list.append(meeting)
    print(condensed_list)


meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
merge_meeting_times(meetings)
