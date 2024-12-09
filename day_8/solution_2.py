from collections import defaultdict

with open("input.txt", "r") as input_file:
    grid = []
    for line in input_file.readlines():
        grid.append(line.rstrip())

    h = len(grid)
    w = len(grid[0])

    antenna_groups = defaultdict(list)
    for y in range(h):
        for x in range(w):
            if grid[y][x] == ".":
                continue
            antenna_type = grid[y][x]
            antenna_pos = (x, y)
            antenna_groups[antenna_type].append(antenna_pos)

    antinodes = set()
    for antenna_positions in antenna_groups.values():
        for i in range(len(antenna_positions)):
            for j in range(i + 1, len(antenna_positions)):
                x_dist = antenna_positions[j][0] - antenna_positions[i][0]
                y_dist = antenna_positions[j][1] - antenna_positions[i][1]

                factor = 0
                while True:
                    new_x = antenna_positions[j][0] + x_dist * factor
                    new_y = antenna_positions[j][1] + y_dist * factor
                    if -1 < new_x < w and -1 < new_y < h:
                        antinodes.add((new_x, new_y))
                        factor += 1
                    else:
                        break

                factor = 0
                while True:
                    new_x = antenna_positions[i][0] - x_dist * factor
                    new_y = antenna_positions[i][1] - y_dist * factor
                    if -1 < new_x < w and -1 < new_y < h:
                        antinodes.add((new_x, new_y))
                        factor += 1
                    else:
                        break

    res = len(antinodes)

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
