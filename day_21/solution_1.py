import itertools


DIRS = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
NUMERIC_TO_POS = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}
DIRECTIONAL_TO_POS = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def is_valid_path(x, y, seq: str, keypad="numeric"):
    gap = (0, 3) if keypad == "numeric" else (0, 0)
    for s in seq:
        x += DIRS[s][0]
        y += DIRS[s][1]
        if (x, y) == gap:
            return False
    return True


def get_options_using_numerical_pad(code: str):
    x, y = 2, 3
    seqs = [""]
    for c in code:
        new_steps = []
        target_x, target_y = NUMERIC_TO_POS[c]
        if target_x == x:
            new_steps = [("v" if y < target_y else "^") * abs(target_y - y) + "A"]
        elif target_y == y:
            new_steps = [(">" if x < target_x else "<") * abs(target_x - x) + "A"]
        else:
            xx = (">" if x < target_x else "<") * abs(target_x - x)
            yy = ("v" if y < target_y else "^") * abs(target_y - y)
            new_steps = ["".join(seq) for seq in set(itertools.permutations(xx + yy))]
            new_steps = [
                seq + "A"
                for seq in new_steps
                if is_valid_path(x, y, seq, keypad="numeric")
            ]

        new_seqs = []
        for s in seqs:
            for ns in new_steps:
                new_seqs.append(s + ns)
        seqs = new_seqs
        x = target_x
        y = target_y

    return seqs


def get_options_using_directional_pad(code: str):
    x, y = 2, 0
    seqs = [""]
    for c in code:
        new_steps = []
        target_x, target_y = DIRECTIONAL_TO_POS[c]
        if target_x == x:
            new_steps = [("v" if y < target_y else "^") * abs(target_y - y) + "A"]
        elif target_y == y:
            new_steps = [(">" if x < target_x else "<") * abs(target_x - x) + "A"]
        else:
            xx = (">" if x < target_x else "<") * abs(target_x - x)
            yy = ("v" if y < target_y else "^") * abs(target_y - y)
            new_steps = ["".join(seq) for seq in set(itertools.permutations(xx + yy))]
            new_steps = [
                seq + "A"
                for seq in new_steps
                if is_valid_path(x, y, seq, keypad="directional")
            ]

        new_seqs = []
        for s in seqs:
            for ns in new_steps:
                new_seqs.append(s + ns)
        seqs = new_seqs
        x = target_x
        y = target_y

    return seqs


def get_control_sequence_len(code):
    robot_1_options = get_options_using_numerical_pad(code)
    me_options = []
    for robot_1_seq in robot_1_options:
        robot_2_options = get_options_using_directional_pad(robot_1_seq)
        for robot_2_seq in robot_2_options:
            robot_3_options = get_options_using_directional_pad(robot_2_seq)
            me_options.extend(robot_3_options)

    return min(len(s) for s in me_options)


with open("input.txt", "r") as input_file:
    res = 0
    for line in input_file.readlines():
        code = line.rstrip()
        control_sequence_len = get_control_sequence_len(code)
        res += int(code[:3]) * control_sequence_len

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
