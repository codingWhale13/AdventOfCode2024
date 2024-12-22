def get_combo_operand(operand, reg_a, reg_b, reg_c):
    if operand in [0, 1, 2, 3]:
        return operand
    elif operand == 4:
        return reg_a
    elif operand == 5:
        return reg_b
    elif operand == 6:
        return reg_c
    raise ValueError(f"operand '{operand}' does not exist")


def run_program(program: list[int], reg_a: int, reg_b: int = 0, reg_c: int = 0):
    output = []
    i = 0  # Instruction pointer
    while i < len(program):
        increase_i_by_2 = True
        opcode, operand = program[i], program[i + 1]
        if opcode == 0:
            numerator = reg_a
            denominator = 2 ** get_combo_operand(operand, reg_a, reg_b, reg_c)
            reg_a = numerator // denominator
        elif opcode == 1:
            reg_b ^= operand
        elif opcode == 2:
            reg_b = get_combo_operand(operand, reg_a, reg_b, reg_c) % 8
        elif opcode == 3:
            if reg_a != 0:
                increase_i_by_2 = False
                i = operand
        elif opcode == 4:
            reg_b ^= reg_c
        elif opcode == 5:
            output.append(get_combo_operand(operand, reg_a, reg_b, reg_c) % 8)
        elif opcode == 6:
            numerator = reg_a
            denominator = 2 ** get_combo_operand(operand, reg_a, reg_b, reg_c)
            reg_b = numerator // denominator
        elif opcode == 7:
            numerator = reg_a
            denominator = 2 ** get_combo_operand(operand, reg_a, reg_b, reg_c)
            reg_c = numerator // denominator
        else:
            raise ValueError(f"found unknwon opcode '{opcode}'")

        if increase_i_by_2:
            i += 2

    return output


def solve_recursively(n: int, program: list[int], d=0):
    if run_program(program, reg_a=n) == program:
        return n

    n <<= 3  # 3 bits in A determine one output value, let's check them all!
    for _ in range(8):
        output = run_program(program, reg_a=n)
        if output == program[-len(output) :]:
            res = solve_recursively(n, program, d + 1)
            if res != -1:
                return res
        n += 1

    return -1


with open("input.txt", "r") as input_file:
    # Read register inputs and program
    lines = input_file.readlines()
    reg_a = int(lines[0].split(":")[1])
    reg_b = int(lines[1].split(":")[1])
    reg_c = int(lines[2].split(":")[1])
    program = list(map(int, lines[4].split(":")[1].split(",")))

    """
    A = ?
    B = 0
    C = 0

    DO
        2,4     B := A%8
        1,3     B := B^3        // flip last two bits of B
        7,5     C := A//(2**B)  // C := A >> B
        0,3     A := A//(2**3)  // A := A >> 3
        4,3     B := B^C
        1,5     B := B^5        // flip last and third-to-last bit of B
        5,5     output B%8
        3,0     WHILE A != 0
    """

    res = solve_recursively(0, program)

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
