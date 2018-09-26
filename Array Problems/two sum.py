from collections import defaultdict


def find_two_movies(duration,timings):
    count_of_timings = defaultdict(int)
    for t in timings:
        count_of_timings[t] += 1
    for t in timings:
        diff = duration - t
        if diff != t and count_of_timings[diff] > 0:
            return True
        if diff == t and count_of_timings[diff] > 1:
            return True

    return False


print(find_two_movies(3,[1,2,1]))