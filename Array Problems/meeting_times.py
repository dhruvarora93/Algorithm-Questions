def meeting_times(ar):
    ar.sort(key=lambda x: x[0])
    start_times = []
    end_times = []
    for i in ar:
        start_times.append(i[0])
        end_times.append(i[1])
    """
    for i in range(1,len(start_times)):
        for j in range(i):
            if start_times[i]<start_times[j]:
                temp=start_times[i]
                start_times[i]=start_times[j]
                start_times[j]=temp
                temp = end_times[i]
                end_times[i] = end_times[j]
                end_times[j] = temp

    print(start_times)
    print(end_times)
    """
    condensed_list=[[start_times[0],end_times[0]]]

    for i in range(1,len(start_times)):
        if start_times[i] <= condensed_list[-1][1]:
            condensed_list[-1] = [condensed_list[-1][0], max(condensed_list[-1][1], end_times[i])]
        else:
            condensed_list.append([start_times[i],end_times[i]])



    print(condensed_list)

meeting_times([[4,5],[1,4],[0,1]])


def minMeetingRooms(intervals):

    if len(intervals) == 0:
        return 0
    start_time = []
    end_time = []
    for i in intervals:
        start_time.append(i[0])
        end_time.append(i[1])

    start_time.sort()
    end_time.sort()
    rooms = 0
    end_index = 0
    for i in start_time:
        if i < end_time[end_index]:
            rooms += 1
        else:
            end_index += 1
    print(rooms)
#minMeetingRooms([[0,30],[5,10],[15,20]])
