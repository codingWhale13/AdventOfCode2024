def route_is_safe(grid, start_x, start_y):
    h = len(grid)
    w = len(grid[0])
    seen_dirs = [[[] for _ in range(w)] for _ in range(h)]

    direction = "U"  # Because of "^" in input
    x, y = start_x, start_y
    while True:
        if direction in seen_dirs[y][x]:
            return True  # We're safe, no out of bounds possible anymore
        seen_dirs[y][x].append(direction)
        
        if direction == "U":
            if y == 0:
                return False  # Next step is out of bounds, we're done
            elif grid[y - 1][x] == "#":
                direction = "R"
            else:
                y -= 1
        elif direction == "R":
            if x == w - 1:
                return False  # Next step is out of bounds, we're done
            elif grid[y][x + 1] == "#":
                direction = "D"
            else:
                x += 1
        elif direction == "D":
            if y == h - 1:
                return False  # Next step is out of bounds, we're done
            elif grid[y + 1][x] == "#":
                direction = "L"
            else:
                y += 1
        elif direction == "L":
            if x == 0:
                return False  # Next step is out of bounds, we're done
            elif grid[y][x - 1] == "#":
                direction = "U"
            else:
                x -= 1


with open("input.txt", "r") as input_file:
    grid = []

    start_x, start_y = None, None
    for y, line in enumerate(input_file.readlines()):
        grid.append([c for c in line.rstrip()])
        if "^" in line:
            start_x = line.find("^")
            start_y = y
            grid[start_y][start_x] = "X"  # Mark all visited spots with X
    h = len(grid)
    w = len(grid[0])

    res = 0  # Number of possible locations to put obstacle to create a loop
    for y in range(h):
        for x in range(w):
            if x == start_x and y == start_y or grid[y][x] == "#":
                continue
            grid[y][x] = "#"  # Place additional obstacle
            if route_is_safe(grid, start_x, start_y):
                res += 1
            grid[y][x] = "."  # Remove obstacle again
            print(res)

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
