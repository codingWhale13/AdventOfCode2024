DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open("input.txt", "r") as input_file:
    # Read input grid and start & target positions
    grid = []  # True = free field, False = wall
    y = 0
    for line in input_file.readlines():
        line = line.rstrip()
        grid.append([c != "#" for c in line])
        if "S" in line:
            start_x = line.find("S")
            start_y = y
        if "E" in line:
            target_x = line.find("E")
            target_y = y
        y += 1
    h, w = len(grid), len(grid[0])
    start_dir = 0  # Start heading east

    # Determine min costs to reach all fields from start position
    min_costs = [[[float("inf") for _ in range(4)] for _ in range(w)] for _ in range(h)]
    min_costs[start_y][start_x][start_dir] = 0

    frontier = [(start_x, start_y, start_dir)]
    while len(frontier) > 0:
        new_frontier = []

        for x, y, d in frontier:
            for nd in range(4):
                if d == (nd + 2) % 4:
                    continue  # Don't turn back since it is never optimal

                nx = x + DIRS[nd][0]
                ny = y + DIRS[nd][1]
                if not grid[ny][nx]:
                    continue  # Can't go through walls - we're not a ghost

                additional_cost = 1 if d == nd else 1001  # 1001 for turn-and-go
                new_cost = min_costs[y][x][d] + additional_cost
                if new_cost < min_costs[ny][nx][nd]:
                    min_costs[ny][nx][nd] = new_cost
                    new_frontier.append((nx, ny, nd))

        frontier = new_frontier

    res = min(min_costs[target_y][target_x][d] for d in range(4))

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
