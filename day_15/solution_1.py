dir_changes = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}

with open("input.txt", "r") as input_file:
    grid = []
    instructions = ""
    read_grid = True
    start_x, start_y = None, None
    for i, line in enumerate(input_file.readlines()):
        line = line.rstrip()
        if len(line) == 0:
            read_grid = False
        elif read_grid:
            grid.append([i for i in line])
            if "@" in line:
                start_x = line.find("@")
                start_y = i
                # Now that we know the start position, don't stand in own way
                grid[start_y][start_x] = "."
        else:
            instructions += line

    h, w = len(grid), len(grid[0])
    x, y = start_x, start_y
    for command in instructions:
        dx, dy = dir_changes[command]

        # Try pushing boxes as neccessary
        success = None
        nx, ny = x, y
        steps_until_free = 0
        while True:
            nx += dx
            ny += dy
            steps_until_free += 1
            if nx == -1 or nx == w or ny == -1 or ny == h or grid[ny][nx] == "#":
                success = False
                break  # Ran into a wall
            if grid[ny][nx] == ".":
                success = True
                break

        # If possible, actually perform the step
        if success:
            if steps_until_free > 1:  # Push box(es)
                grid[y + dy * steps_until_free][x + dx * steps_until_free] = "O"
                grid[y + dy][x + dx] = "."
            x += dx
            y += dy

    res = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "O":
                gps_coordinate = y * 100 + x
                res += gps_coordinate

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
