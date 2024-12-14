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
        prize = (int(prize_raw[1][2:-1]), int(prize_raw[2][2:]))

        done = False
        for a_count in range(100):
            x = button_a[0] * a_count
            y = button_a[1] * a_count
            for b_count in range(100):
                x_final = x + button_b[0] * b_count
                y_final = y + button_b[1] * b_count
                if (x_final, y_final) == prize:
                    res += a_count * a_cost + b_count * b_cost
                    done = True
                    break
            if done:
                break

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
