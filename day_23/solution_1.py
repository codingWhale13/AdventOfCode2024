with open("input.txt", "r") as input_file:
    g = {}
    for line in input_file.readlines():
        a, b = line.rstrip().split("-")
        if a not in g:
            g[a] = set()
        if b not in g:
            g[b] = set()
        g[a].add(b)
        g[b].add(a)

    res = 0  # Number of 3-groups of fully connected players
    names = list(g.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if names[j] not in g[names[i]]:
                continue  # These two computers aren't conntected
            for k in range(j + 1, len(names)):
                if not any(names[idx].startswith("t") for idx in [i, j, k]):
                    continue  # Chief can't be here
                if names[k] in g[names[i]] and names[k] in g[names[j]]:
                    res += 1

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
