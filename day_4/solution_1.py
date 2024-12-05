XMAS = "XMAS"

with open("input.txt", "r") as input_file:
    grid = list(input_file.readlines())
    h, w = len(grid), len(grid[0])

    xmas_count = 0
    for y in range(h):
        for x in range(w):
            # Search left-to-right
            if (
                x + 3 < w
                and grid[y][x] + grid[y][x + 1] + grid[y][x + 2] + grid[y][x + 3]
                == XMAS
            ):
                xmas_count += 1

            # Search right-to-left
            if (
                x - 3 >= 0
                and grid[y][x] + grid[y][x - 1] + grid[y][x - 2] + grid[y][x - 3]
                == XMAS
            ):
                xmas_count += 1

            # Search top-to-bottom
            if (
                y + 3 < h
                and grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x]
                == XMAS
            ):
                xmas_count += 1

            # Search bottom-to-top
            if (
                y - 3 >= 0
                and grid[y][x] + grid[y - 1][x] + grid[y - 2][x] + grid[y - 3][x]
                == XMAS
            ):
                xmas_count += 1

            # Search diagonally right and down
            if (
                x + 3 < w
                and y + 3 < h
                and grid[y][x]
                + grid[y + 1][x + 1]
                + grid[y + 2][x + 2]
                + grid[y + 3][x + 3]
                == XMAS
            ):
                xmas_count += 1

            # Search diagonally right and up
            if (
                x + 3 < w
                and y - 3 >= 0
                and grid[y][x]
                + grid[y - 1][x + 1]
                + grid[y - 2][x + 2]
                + grid[y - 3][x + 3]
                == XMAS
            ):
                xmas_count += 1

            # Search diagonally left and down
            if (
                x - 3 >= 0
                and y + 3 < h
                and grid[y][x]
                + grid[y + 1][x - 1]
                + grid[y + 2][x - 2]
                + grid[y + 3][x - 3]
                == XMAS
            ):
                xmas_count += 1

            # Search diagonally left and and up
            if (
                x - 3 >= 0
                and y - 3 >= 0
                and grid[y][x]
                + grid[y - 1][x - 1]
                + grid[y - 2][x - 2]
                + grid[y - 3][x - 3]
                == XMAS
            ):
                xmas_count += 1

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(xmas_count))
