def max_points(points):

    if len(points) == 0:
        return 0

    count_of_points = {}

    for p in points:
        count_of_points[(p[0], p[1])] = count_of_points.get((p[0], p[1]), 0) + 1

    keys = list(count_of_points.keys())

    if len(keys) == 1:
        return count_of_points[keys[0]]

    max_points = float('-inf')

    for i in range(len(keys)-1):
        slopes = {}
        for j in range(i+1, len(keys)):
            dx, dy = keys[i][0] - keys[j][0], keys[i][1] - keys[j][1]
            if dx == 0:
                slope = '#'
            elif dy == 0:
                slope = 0
            else:
                slope = float(dy) / dx
            slopes[slope] = slopes.get(slope, 0) + count_of_points[keys[j]]

        max_points = max(max_points, max(slopes.values()) + count_of_points[keys[i]])

    return max_points


pts = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4],[3,2],[3,2]]
print(max_points(pts))