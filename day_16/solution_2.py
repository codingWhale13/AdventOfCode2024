DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_min_costs(grid, start_x, start_y, start_dir):
    h, w = len(grid), len(grid[0])
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

                if d == nd:  #  Case 1: go straight ahead
                    additional_cost = 1
                    new_cost = min_costs[y][x][d] + additional_cost
                    if new_cost < min_costs[ny][nx][nd]:
                        min_costs[ny][nx][nd] = new_cost
                        new_frontier.append((nx, ny, nd))
                else:  # Case 2: turn on the spot
                    additional_cost = 1000
                    new_cost = min_costs[y][x][d] + additional_cost
                    if new_cost < min_costs[y][x][nd]:
                        min_costs[y][x][nd] = new_cost
                        new_frontier.append((x, y, nd))

        frontier = new_frontier

    return min_costs


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
    # (start_dir when beginning from target is input-specific, here start_dir=1)
    start_to_target_costs = get_min_costs(grid, start_x, start_y, start_dir=0)
    target_to_start_costs = get_min_costs(grid, target_x, target_y, start_dir=1)
    optimal_cost = min(start_to_target_costs[target_y][target_x][d] for d in range(4))

    res = 0  # Number of cells on any optimal path from start to target
    for y in range(h):
        for x in range(w):
            is_optimal_seat = False
            for d in range(4):
                if (
                    start_to_target_costs[y][x][d]
                    + target_to_start_costs[y][x][(d + 2) % 4]
                    == optimal_cost
                ):
                    is_optimal_seat = True
            if is_optimal_seat:
                res += 1

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
