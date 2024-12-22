def possible(target: str, patterns: list[str]):
    possible_starts = [False for _ in range(len(target) + 1)]

    todo = [0]  # positions where new pattern can be started
    while len(todo) > 0:
        new_todo = []
        for start_pos in todo:
            possible_starts[start_pos] = True
            for pattern in patterns:
                new_start_pos = start_pos + len(pattern)
                if (
                    target[start_pos:new_start_pos] == pattern
                    and not possible_starts[new_start_pos]
                ):
                    possible_starts[new_start_pos] = True
                    new_todo.append(new_start_pos)
        todo = new_todo

    return possible_starts[len(target)]


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    patterns = [line for line in lines[0].rstrip().split(", ")]

    res = 0
    for testcase in range(2, len(lines)):
        target = lines[testcase].rstrip()
        if possible(target, patterns):
            res += 1

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
