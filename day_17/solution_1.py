def get_combo_operand(operand):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    raise ValueError(f"operand '{operand}' does not exist")


with open("input.txt", "r") as input_file:
    # Read register inputs and program
    lines = input_file.readlines()
    reg_a = int(lines[0].split(":")[1])
    reg_b = int(lines[1].split(":")[1])
    reg_c = int(lines[2].split(":")[1])
    program = list(map(int, lines[4].split(":")[1].split(",")))

    # Execute program
    output = []
    i = 0  # instruction pointer
    while i < len(program):
        increase_i_by_2 = True
        opcode, operand = program[i], program[i + 1]
        if opcode == 0:
            numerator = reg_a
            denominator = 2 ** get_combo_operand(operand)
            reg_a = numerator // denominator
        elif opcode == 1:
            reg_b ^= operand
        elif opcode == 2:
            reg_b = get_combo_operand(operand) % 8
        elif opcode == 3:
            if reg_a != 0:
                increase_i_by_2 = False
                i = operand
        elif opcode == 4:
            reg_b ^= reg_c
        elif opcode == 5:
            output.append(get_combo_operand(operand) % 8)
        elif opcode == 6:
            numerator = reg_a
            denominator = 2 ** get_combo_operand(operand)
            reg_b = numerator // denominator
        elif opcode == 7:
            numerator = reg_a
            denominator = 2 ** get_combo_operand(operand)
            reg_c = numerator // denominator
        else:
            raise ValueError(f"found unknwon opcode '{opcode}'")

        if increase_i_by_2:
            i += 2

    res = ",".join(map(str, output))

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
