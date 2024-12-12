with open("input.txt", "r") as input_file:
    stones = {}  # Format: value -> amount
    for stone in map(int, input_file.readlines()[0].split()):
        stones[stone] = stones.get(stone, 0) + 1

    blink_count = 75
    for i in range(blink_count):
        new_stones = {}
        for value, amount in stones.items():
            value_str = str(value)
            if value == 0:
                new_stones[1] = new_stones.get(1, 0) + amount
            elif len(value_str) % 2 == 0:
                half_len = len(value_str) // 2
                l, r = int(value_str[:half_len]), int(value_str[half_len:])
                new_stones[l] = new_stones.get(l, 0) + amount
                new_stones[r] = new_stones.get(r, 0) + amount
            else:
                new_stones[value * 2024] = new_stones.get(stone * 2024, 0) + amount
        stones = new_stones
    res = sum(stones.values())

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
