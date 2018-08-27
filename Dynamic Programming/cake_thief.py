def max_duffel_bag_value_with_capacity(cake_tuples, capacity, max_at_each_weight):
    for i in range(1,capacity+1):
        maximum = 0
        for cake_weight, cake_value in cake_tuples:
            if cake_weight <= i and cake_weight != 0:
                current = max(cake_value, cake_value + max_at_each_weight[i-cake_weight])
                maximum = max(maximum, current)

        max_at_each_weight.append(maximum)

    #print(max_at_each_weight)

    return max_at_each_weight[-1]


max_at_each = [0]
cake_tuples = [(0, 0), (3, 90), (2, 15)]
capacity = 20
print(max_duffel_bag_value_with_capacity(cake_tuples,capacity,max_at_each))