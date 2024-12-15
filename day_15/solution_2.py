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
            row = []
            for j, c in enumerate(line):
                if c == "#":
                    row.extend(["#", "#"])
                elif c == ".":
                    row.extend([".", "."])
                elif c == "@":
                    start_x = j * 2
                    start_y = i
                    row.extend([".", "."])
                elif c == "O":
                    row.extend(["L", "R"])
            grid.append(row)
        else:
            instructions += line
    h, w = len(grid), len(grid[0])

    x, y = start_x, start_y
    for command in instructions:
        dx, dy = dir_changes[command]

        nx = x + dx
        ny = y + dy
        if grid[ny][nx] == "#":  # Easy case: blocked by wall
            continue  # Can't go
        elif grid[ny][nx] == ".":  # Easy case: free to go
            x, y = nx, ny
        else:  # Harder case: Push boxes around
            possible = True
            affected_boxes = []  # Left side of LR boxes to be moved
            positions_to_check = [(nx, ny)]
            while len(positions_to_check) > 0:
                x_check, y_check = positions_to_check.pop()
                if grid[y_check][x_check] == "#":
                    possible = False  # Box cannot be moved into wall
                    break
                elif grid[y_check][x_check] == "L":
                    affected_boxes.append((x_check, y_check))

                    if dx == -1 and dy == 0:  # LR<--
                        assert False, "This case should not occur"
                    elif dx == 1 and dy == 0:  # -->LR
                        positions_to_check.append((x_check + 2, y_check))
                    else:
                        positions_to_check.append((x_check + dx, y_check + dy))
                        positions_to_check.append((x_check + 1 + dx, y_check + dy))
                elif grid[y_check][x_check] == "R":
                    affected_boxes.append((x_check - 1, y_check))
                    if dx == -1 and dy == 0:  # LR<--
                        positions_to_check.append((x_check - 2, y_check))
                    elif dx == 1 and dy == 0:  # -->LR
                        assert False, "This case should not occur"
                    else:
                        positions_to_check.append((x_check + dx, y_check + dy))
                        positions_to_check.append((x_check - 1 + dx, y_check + dy))
                elif grid[y_check][x_check] == ".":
                    pass  # Nothing to do, a box can be easily moved onto this field

            if possible:
                new_grid = [["." for _ in range(w)] for _ in range(h)]
                for yy in range(h):
                    for xx in range(w):
                        if grid[yy][xx] == "#":
                            new_grid[yy][xx] = "#"  # Walls remain walls
                        elif grid[yy][xx] == "L":
                            if (xx, yy) in affected_boxes:  # Box is now moved
                                new_grid[yy + dy][xx + dx] = "L"
                                new_grid[yy + dy][xx + 1 + dx] = "R"
                            else:  # Box remains at same position
                                new_grid[yy][xx] = "L"
                                new_grid[yy][xx + 1] = "R"
                        else:
                            pass  # Empty places "." are default, "R" is handled above

                grid = new_grid
                x += dx
                y += dy
            else:
                pass  # Action cannot be performed because at least one box is stuck

    res = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "L":
                gps_coordinate = y * 100 + x
                res += gps_coordinate

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
