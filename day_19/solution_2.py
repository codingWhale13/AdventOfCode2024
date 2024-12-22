def possibility_count(target: str, patterns: list[str]):
    possible_starts = [0 for _ in range(len(target))] + [1]

    for start_pos in range(len(target) - 1, -1, -1):
        for pattern in patterns:
            next_start_pos = start_pos + len(pattern)
            if target[start_pos:next_start_pos] == pattern:
                possible_starts[start_pos] += possible_starts[next_start_pos]

    return possible_starts[0]


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    patterns = [line for line in lines[0].rstrip().split(", ")]

    res = 0
    for testcase in range(2, len(lines)):
        target = lines[testcase].rstrip()
        c = possibility_count(target, patterns)
        res += c

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
