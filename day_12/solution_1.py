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


def get_perimeter(garden, region):
    h, w = len(garden), len(garden[0])
    plant_type = garden[region[0][1]][region[0][0]]
    perimeter = 0
    for x, y in region:
        for d in DIRS:
            nx, ny = x + d[0], y + d[1]
            if (
                nx == -1
                or nx == w
                or ny == -1
                or ny == h
                or garden[ny][nx] != plant_type
            ):
                perimeter += 1

    return perimeter


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
            perimeter = get_perimeter(garden, region)
            res += area * perimeter

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
