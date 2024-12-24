DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MIN_CHEAT_REQUIREMENT = 100


def get_path(
    grid,
    start: tuple[int, int],
    target: tuple[int, int],
    normal_mode: bool = True,
    max_steps: int = 999999999,
) -> list[tuple[int, int]]:
    # BFS
    # normal_mode=True: only use non-wall tiles
    # normal_mode=False: only use wall-tiles (except start and target)
    h = len(grid)
    w = len(grid[0])

    frontier = [start]
    previous = {start: start}
    step_count = 0

    while len(frontier) > 0 and step_count <= max_steps:
        new_frontier = []
        for pos in frontier:
            if pos == target:
                # Reconstruct path
                reverse_path = [pos]
                while pos != start:
                    pos = previous[pos]
                    reverse_path.append(pos)

                return reverse_path[::-1]
            for d in DIRS:
                nx, ny = pos[0] + d[0], pos[1] + d[1]
                if (
                    -1 < nx < w
                    and -1 < ny < h
                    and ((grid[ny][nx] == normal_mode) or (nx, ny) == target)
                    and (nx, ny) not in previous
                ):
                    previous[(nx, ny)] = pos
                    new_frontier.append((nx, ny))

        frontier = new_frontier
        step_count += 1

    return None


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

    path = get_path(grid, start, target)  # Path without cheats

    time_saves = {}

    res = 0  # Will countain number of cheats saving 100+ picoseconds
    for i in range(len(path)):
        print("!", i)
        for j in range(
            i + MIN_CHEAT_REQUIREMENT, len(path)
        ):  # We want to skip at least 100 cells
            # Consider skipping from path[i] to path[j]
            start = path[i]
            target = path[j]
            cheat_steps = abs(target[0] - start[0]) + abs(target[1] - start[1])
            if cheat_steps <= 20:
                original_time_saved = j - i
                time_benefit = original_time_saved - cheat_steps
                if time_benefit >= MIN_CHEAT_REQUIREMENT:
                    if time_benefit not in time_saves:
                        time_saves[time_benefit] = 0
                    time_saves[time_benefit] += 1
                    res += 1

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
