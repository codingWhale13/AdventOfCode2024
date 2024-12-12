DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def get_region(garden, visited, start_x, start_y):
    h, w = len(garden), len(garden[0])
    plant_type = garden[start_y][start_x]
    region = [(start_x, start_y)]  # Positions within this region
    frontier = [(start_x, start_y)]
    visited[start_y][start_x] = True
    while len(frontier) > 0:
        new_frontier = []
        for x, y in frontier:
            for d in DIRS:
                nx, ny = x + d[0], y + d[1]
                if nx == -1 or nx == w or ny == -1 or ny == h or visited[ny][nx]:
                    continue
                if garden[ny][nx] == plant_type:
                    visited[ny][nx] = True
                    new_frontier.append((nx, ny))
                    region.append((nx, ny))
        frontier = new_frontier

    return region


def get_side_count(garden, region):
    # First point in region always starts a top side going to the right.
    # Let's follow it until we've gone all the way around the region clockwise

    h, w = len(garden), len(garden[0])
    plant_type = garden[region[0][1]][region[0][0]]
    side_count = 0

    done = set()
    for x, y in region:
        for side in ["up", "down", "right", "left"]:
            if (
                not (
                    side == "up"
                    and (y == 0 or garden[y - 1][x] != plant_type)
                    or side == "down"
                    and (y == h - 1 or garden[y + 1][x] != plant_type)
                    or side == "left"
                    and (x == 0 or garden[y][x - 1] != plant_type)
                    or side == "right"
                    and (x == w - 1 or garden[y][x + 1] != plant_type)
                )
                or (x, y, side) in done
            ):
                continue

            done.add((x, y, side))
            side_count += 1

            while True:
                # Take a step along the edge (not neccessarily a change in position)
                new_side = side
                if side == "up":
                    if x == w - 1:
                        new_side = "right"
                    elif garden[y][x + 1] != plant_type:
                        new_side = "right"
                    elif y > 0 and garden[y - 1][x + 1] == plant_type:
                        x += 1
                        y -= 1
                        new_side = "left"
                    else:
                        x += 1
                elif side == "right":
                    if y == h - 1:
                        new_side = "down"
                    elif garden[y + 1][x] != plant_type:
                        new_side = "down"
                    elif x < w - 1 and garden[y + 1][x + 1] == plant_type:
                        x += 1
                        y += 1
                        new_side = "up"
                    else:
                        y += 1
                elif side == "down":
                    if x == 0:
                        new_side = "left"
                    elif garden[y][x - 1] != plant_type:
                        new_side = "left"
                    elif y < h - 1 and garden[y + 1][x - 1] == plant_type:
                        x -= 1
                        y += 1
                        new_side = "right"
                    else:
                        x -= 1
                elif side == "left":
                    if y == 0:
                        new_side = "up"
                    elif garden[y - 1][x] != plant_type:
                        new_side = "up"
                    elif x > 0 and garden[y - 1][x - 1] == plant_type:
                        x -= 1
                        y -= 1
                        new_side = "down"
                    else:
                        y -= 1

                # Update side info
                if side != new_side:
                    side_count += 1
                side = new_side

                if (x, y, side) in done:
                    side_count -= 1
                    break  # Went full cirle
                done.add((x, y, side))

    return side_count


with open("input.txt", "r") as input_file:
    garden = []
    for line in input_file.readlines():
        garden.append([s for s in line.rstrip()])

    h = len(garden)
    w = len(garden[0])

    visited = [[False for _ in range(w)] for _ in range(h)]
    res = 0
    for y in range(h):
        for x in range(w):
            if visited[y][x]:
                continue
            region = get_region(garden, visited, x, y)
            area = len(region)
            side_count = get_side_count(garden, region)
            res += area * side_count

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
