DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


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

    return None


with open("input.txt", "r") as input_file:
    blocks = []
    for line in input_file.readlines():
        x, y = map(int, line.split(","))
        blocks.append((x, y))

    h, w = 71, 71
    grid = [[True for _ in range(w)] for _ in range(h)]
    for x, y in blocks:
        grid[y][x] = False
        if min_steps(grid, (0, 0), (w - 1, h - 1)) is None:
            res = f"{x},{y}"
            break

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
