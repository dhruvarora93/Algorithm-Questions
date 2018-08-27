def reconstruct_queue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people = sorted(people, key=lambda x: (x[0]),reverse=True)
    ret_list = []
    for person in people:
        ret_list.insert(person[1], person)
    # print ret_list
    return ret_list



print(reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))

print([[1,2,3]])