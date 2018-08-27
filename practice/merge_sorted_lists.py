def merge_sorted_lists(list1,list2):

    merged_list = [None] * (len(list1) + len(list2))
    first_list_index = 0
    second_list_index = 0
    merged_list_index = 0
    while merged_list_index < len(merged_list):
        isfirst = first_list_index < len(list1)
        issecond = second_list_index < len(list2)

        if isfirst and (not issecond or list1[first_list_index] < list2[second_list_index]):
            merged_list[merged_list_index] = list1[first_list_index]
            first_list_index += 1
        else:
            merged_list[merged_list_index] = list2[second_list_index]
            second_list_index += 1

        merged_list_index += 1

    print(merged_list)


merge_sorted_lists([3, 4, 6, 10, 11, 15],[1, 5, 8, 12, 14, 19,20,21,22,23])

