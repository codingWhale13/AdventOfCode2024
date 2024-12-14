def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def solve(button_a, button_b, t):
    ax, ay = button_a
    bx, by = button_b
    tx, ty = t

    ax_ay_lcm = lcm(ax, ay)

    mult_1 = ax_ay_lcm // ax  # Factor with which to multiply equation (1)
    mult_2 = ax_ay_lcm // ay  # Factor with which to multiply equation (2)

    # We have two equations and two unknowns (a and b):
    # (1) a*ax + b*bx = tx  <-- multiply by mult_1
    # (2) a*ay + b*by = ty  <-- multiply by mult_2
    # Then subtract (2) from (1) to get left_side=right_side (1 equation, 1 unkown)

    left_side = mult_1 * bx - mult_2 * by
    right_side = mult_1 * tx - mult_2 * ty
    if left_side == 0:
        return None, None

    if right_side % left_side != 0:
        return None, None

    b = right_side // left_side
    a_ax = tx - b * bx
    if a_ax % ax == 0:
        a = a_ax // ax
        return a, b

    return None, None


a_cost = 3
b_cost = 1

with open("input.txt", "r") as input_file:
    res = 0
    lines = input_file.readlines()
    for i in range(0, len(lines), 4):
        button_a_raw = lines[i].split()
        button_b_raw = lines[i + 1].split()
        prize_raw = lines[i + 2].split()

        button_a = (int(button_a_raw[2][2:-1]), int(button_a_raw[3][2:]))
        button_b = (int(button_b_raw[2][2:-1]), int(button_b_raw[3][2:]))
        prize = (
            10000000000000 + int(prize_raw[1][2:-1]),
            10000000000000 + int(prize_raw[2][2:]),
        )

        a, b = solve(button_a, button_b, prize)
        if a is not None:
            res += a * a_cost + b * b_cost

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
