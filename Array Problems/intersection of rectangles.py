def find_overlap(point1,length1,point2,length2):
    highest_point = max(point1,point2)
    lowest_point = min(point1+length1,point2+length2)

    if highest_point >= lowest_point:
        return (None,None)

    return highest_point, lowest_point - highest_point





my_rectangle1 = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}
my_rectangle2 = {

    # Coordinates of bottom-left corner
    'left_x'   : 8,
    'bottom_y' : 1,

    # Width and height
    'width'    : 2,
    'height'   : 1,

}

find_overlap(my_rectangle1,my_rectangle2)


