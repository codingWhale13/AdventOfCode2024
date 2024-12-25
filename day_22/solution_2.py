MOD = 16777216


def get_price_data(value, n=2000):
    prices = [value % 10]
    price_changes = []
    for _ in range(n):
        value = (value ^ (value * 64)) % MOD
        value = (value ^ (value // 32)) % MOD
        value = (value ^ (value * 2048)) % MOD

        prices.append(value % 10)
        price_changes.append(prices[-1] - prices[-2])

    return prices, price_changes


with open("input.txt", "r") as input_file:
    rewards = {}  # Mappings from 4-char string to banana count
    for line in input_file.readlines():
        seed = int(line)
        prices, price_changes = get_price_data(seed)
        used_sequences = set()  # Make sure only first sequence counts
        for i in range(4, len(price_changes) + 1):
            sequence = "".join(map(str, price_changes[i - 4 : i]))
            if sequence not in rewards:
                rewards[sequence] = 0
            if sequence not in used_sequences:
                rewards[sequence] += prices[i]
                used_sequences.add(sequence)

    res = max(rewards.values())  # max banana count possible

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
