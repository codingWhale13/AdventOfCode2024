with open("input.txt", "r") as input_file:
    grid = list(input_file.readlines())
    h, w = len(grid), len(grid[0])

    xmas_count = 0
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if (
                grid[y][x] == "A"
                and (grid[y - 1][x - 1] + grid[y + 1][x + 1] in ["MS", "SM"])
                and (grid[y - 1][x + 1] + grid[y + 1][x - 1] in ["MS", "SM"])
            ):
                xmas_count += 1

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(xmas_count))
