def find_largest_product(lst):

    largest = max(lst[0],lst[1])
    smallest = min(lst[0],lst[1])

    highest_product_of_2 = lst[0]*lst[1]
    lowest_product_of_2 = lst[0]*lst[1]

    highest_product_of_3=lst[0]*lst[1]*lst[2]

    for i in range(2,len(lst)):
        current = lst[i]

        highest_product_of_3=max(highest_product_of_3,current*highest_product_of_2,current*lowest_product_of_2)

        highest_product_of_2=max(highest_product_of_2,current*largest,current*smallest)

        lowest_product_of_2=min(lowest_product_of_2,current*largest,current*smallest)

        largest = max(largest, current)

        smallest=min(smallest,current)

    return highest_product_of_3

print(find_largest_product([1,10,-5,-3]))
