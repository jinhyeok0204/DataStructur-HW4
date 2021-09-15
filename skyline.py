import heapq


def get_skyline_points(buildings: 'List[List[int]]') -> 'List[List[int]]':
    events = [[L, -H, R] for L, R, H in buildings]

    events += [[R, 0, 0] for _, R, _ in buildings]
    events.sort()
    result = [[0, 0]]  # [x, height]
    now = [(0, float('inf'))]  # (-height, x)

    for pos, neg_h, R in events:
        while now[0][1] <= pos:
            heapq.heappop(now)
        if neg_h:
            heapq.heappush(now, (neg_h, R))
            print(now)
        if result[-1][1] != -now[0][0]:
            result.append([pos, -now[0][0]])
    return result[1:]


def print_skyline(sky_line_points: 'List[List[int]]'):
    sky_line = []
    points_len = len(sky_line_points)
    for i in range(0, points_len - 1):
        x_diff = sky_line_points[i+1][0] - sky_line_points[i][0]
        y_diff = sky_line_points[i+1][1] - sky_line_points[i][1]
        if x_diff != 0:
            sky_line.append(x_diff)
        if y_diff != 0:
            sky_line.append(y_diff)
    print(*sky_line)


def main():
    num_building = int(input())
    buildings = []
    for i in range(num_building):
        l, h, w = list(map(int, input().split()))
        buildings.append([l, l+w, h])
    sky_line_points = [[0, 0]] + get_skyline_points(buildings)
    print_skyline(sky_line_points)


if __name__ == '__main__':
    main()
