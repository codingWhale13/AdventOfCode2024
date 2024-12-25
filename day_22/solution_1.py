MOD = 16777216


def evolve(value, n):
    for _ in range(n):
        value = (value ^ (value * 64)) % MOD
        value = (value ^ (value // 32)) % MOD
        value = (value ^ (value * 2048)) % MOD

    return value


with open("input.txt", "r") as input_file:
    res = 0
    for line in input_file.readlines():
        seed = int(line)
        res += evolve(seed, 2000)

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
