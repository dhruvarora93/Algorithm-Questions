def walking_soln(arr):

    arr = sorted(arr)

    for i,s in enumerate(arr):
        min_index = i
        max_index = len(arr) - 1

        while min_index <= max_index:

            if arr[min_index] + arr[max_index] > -s:
                max_index -= 1

            elif arr[min_index] + arr[max_index] < -s:
                min_index += 1

            else:
                print(s,arr[min_index],arr[max_index])
                break


walking_soln([-1, 0, 1, 2, -1, -4])
