def least_interval(tasks,n):
    count = {}
    for task in tasks:
        if task not in count:
            count[task] = 1
        else:
            count[task] += 1
    max_value = 0
    max_key = ""
    for key, value in count.items():
        if value > max_value:
            max_value = value
            max_key = key
    max_value -= 1
    idle_slots = max_value * n
    for key,value in count.items():
        if key != max_key and idle_slots:
            idle_slots -= min(value,max_value)

    if idle_slots < 0 :idle_slots = 0
    return len(tasks) + idle_slots

print(least_interval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))