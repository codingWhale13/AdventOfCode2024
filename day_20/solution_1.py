DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def min_steps(grid, start, target):
    # BFS
    h = len(grid)
    w = len(grid[0])

    frontier = [start]
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[start[1]][start[0]] = True

    step_count = 0
    while len(frontier) > 0:
        new_frontier = []
        for pos in frontier:
            if pos == target:
                return step_count
            for d in DIRS:
                nx, ny = pos[0] + d[0], pos[1] + d[1]
                if -1 < nx < w and -1 < ny < h and grid[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    new_frontier.append((nx, ny))

        frontier = new_frontier
        step_count += 1


with open("input.txt", "r") as input_file:
    # Read input grid and start & target positions
    grid = []  # True = free field, False = wall
    y = 0
    for line in input_file.readlines():
        line = line.rstrip()
        grid.append([c != "#" for c in line])
        if "S" in line:
            start = (line.find("S"), y)
        if "E" in line:
            target = (line.find("E"), y)
        y += 1

    h = len(grid)
    w = len(grid[0])
    original_cost = min_steps(grid, start, target)
    res = 0  # Will countain number of cheats saving 100+ picoseconds
    for y in range(h):
        for x in range(w):
            if not grid[y][x]:
                grid[y][x] = True  # Remove wall
                time_benefit = original_cost - min_steps(grid, start, target)
                if time_benefit >= 100:
                    res += 1
                grid[y][x] = False  # Replace wall again

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
