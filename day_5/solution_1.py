with open("input.txt", "r") as input_file:
    rules = []  # (A, B) -> A before B
    updates = []
    read_rules = True
    for line in input_file.readlines():
        if line == "\n":
            read_rules = False
        elif read_rules:
            a, b = line.split("|")
            rules.append((int(a), int(b)))
        else:
            updates.append([int(i) for i in line.split(",")])

    # BRUTE FORCE, YAY :)
    res = 0
    for update in updates:
        correct = True
        for i in range(len(update)):
            for j in range(i + 1, len(update)):
                a = update[i]
                b = update[j]
                if (b, a) in rules:
                    correct = False
                    break
            if not correct:
                break
        if correct:
            res += update[len(update) // 2]

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
