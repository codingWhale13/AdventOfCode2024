def count_reachable_peaks(grid, start_x, start_y):
    # BFS
    h = len(grid)
    w = len(grid[0])

    frontier = [(start_x, start_y)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[start_y][start_x] = True
    peaks_found = 0

    while len(frontier) > 0:
        new_frontier = []
        for x, y in frontier:
            if grid[y][x] == 9:
                peaks_found += 1
                continue
            for xd, yd in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx = x + xd
                ny = y + yd
                if -1 < nx < w and -1 < ny < h and not visited[ny][nx] and grid[ny][nx] == grid[y][x] + 1:
                    new_frontier.append((nx, ny))
                    visited[ny][nx] = True
        frontier = new_frontier

    print(peaks_found)
    return peaks_found


with open("input.txt", "r") as input_file:
    grid = []
    for line in input_file.readlines():
        grid.append([int(x) for x in line.rstrip()])

    h = len(grid)
    w = len(grid[0])
    res = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 0:
                res += count_reachable_peaks(grid, x, y)

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
