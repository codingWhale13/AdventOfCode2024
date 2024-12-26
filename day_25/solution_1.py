with open("input.txt", "r") as input_file:
    grid = []
    locks, keys = [], []
    for line in input_file.readlines() + ["\n"]:
        if line == "\n":
            counts = [
                (sum(int(grid[y][x] == "#") for y in range(len(grid)))) - 1
                for x in range(len(grid[0]))
            ]
            print(counts)

            if grid[0][0] == "#":  # Lock
                locks.append(counts)
            else:
                keys.append(counts)
            grid = []
        else:
            grid.append(line.rstrip())

    res = 0
    for key in keys:
        for lock in locks:
            possible_match = True
            for i in range(len(key)):
                if key[i] + lock[i] > 5:
                    possible_match = False
            if possible_match:
                res += 1

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
