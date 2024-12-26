INPUT = "INP"


def propagate_state(g, state):
    return state


def get_state(g, key):
    instr = g[key][0]
    if instr == INPUT:
        return g[key][1]

    a, b = g[key][1], g[key][2]
    if instr == "AND":
        return get_state(g, a) & get_state(g, b)
    if instr == "OR":
        return get_state(g, a) | get_state(g, b)
    if instr == "XOR":
        return get_state(g, a) ^ get_state(g, b)


with open("input.txt", "r") as input_file:
    read_start_bits = True
    g = {}
    for line in input_file.readlines():
        if line == "\n":
            read_start_bits = False
        elif read_start_bits:
            wire_name, bit = line.split(": ")
            g[wire_name] = (INPUT, int(bit))
        else:
            a, instruction, b, _, wire_out = line.split()
            g[wire_out] = (instruction, a, b)

    bit_str_reverse = ""
    for k in sorted([k for k in g.keys() if k[0] == "z"], key=lambda x: int(x[1:])):
        bit_str_reverse += str(get_state(g, k))

    res = int(bit_str_reverse[::-1], base=2)

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
