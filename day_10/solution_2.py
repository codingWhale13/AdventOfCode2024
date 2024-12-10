def get_rating(grid, x, y, value=0):
    # DFS
    if grid[y][x] == 9:
        return 1  # We completed a trail

    h = len(grid)
    w = len(grid[0])

    res = 0
    for xd, yd in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx = x + xd
        ny = y + yd
        if -1 < nx < w and -1 < ny < h and grid[ny][nx] == grid[y][x] + 1:
            res += get_rating(grid, nx, ny, value + 1)
    return res


with open("input.txt", "r") as input_file:
    grid = []
    for line in input_file.readlines():
        grid.append([int(x) for x in line.rstrip()])

    h = len(grid)
    w = len(grid[0])
    res = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 0:
                res += get_rating(grid, x, y)

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
