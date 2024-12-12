with open("input.txt", "r") as input_file:
    stones = [int(i) for i in input_file.readlines()[0].split()]

    blink_count = 25
    for i in range(blink_count):
        new_stones = []
        for s in stones:
            s_str = str(s)
            if s == 0:
                new_stones.append(1)
            elif len(s_str) % 2 == 0:
                half_len = len(s_str) // 2
                l, r = s_str[:half_len], s_str[half_len:]
                new_stones.extend([int(l), int(r)])
            else:
                new_stones.append(s * 2024)
        stones = new_stones

    res = len(stones)

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
