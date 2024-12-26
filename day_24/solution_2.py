# This code is essentially copy-pasted from a neat solution:
# https://github.com/guohao/advent-of-code/blob/main/2024/day24/part2.py
# I just wanted to finnish this lovely calendar sooner rather than later this year :)


def minmax(a, b):
    return (a, b) if a <= b else (b, a)


def swap(g, rg, a, b):
    rg[a], rg[b] = rg[b], rg[a]
    g[rg[a]], g[rg[b]] = g[rg[b]], g[rg[a]]


with open("input.txt", "r") as input_file:
    read_start_bits = True
    g, rg = {}, {}  # Forward and reverse graph
    for line in input_file.readlines():
        if line == "\n":
            read_start_bits = False
        elif not read_start_bits:
            a, instruction, b, _, wire_out = line.split()
            a, b = minmax(a, b)
            g[a, b, instruction] = wire_out
            rg[wire_out] = a, b, instruction

    output = set()
    carry = g["x00", "y00", "AND"]
    for i in range(1, int(max(rg.keys())[1:])):
        x = f"x{i:02}"
        y = f"y{i:02}"
        z = f"z{i:02}"
        zn = f"z{i + 1:02}"
        xxy = g[x, y, "XOR"]
        xay = g[x, y, "AND"]
        a, b = minmax(carry, xxy)
        k = a, b, "XOR"
        if k not in g:
            a, b = list(set(rg[z][:2]) ^ set(k[:2]))
            output.update({a, b})
            swap(g, rg, a, b)
        elif g[k] != z:
            output.update({g[k], z})
            swap(g, rg, z, g[k])

        # Let's continue certainly properly
        k = rg[z]
        xxy = g[x, y, "XOR"]
        xay = g[x, y, "AND"]
        carry = g[*minmax(carry, xxy), "AND"]
        carry = g[*minmax(carry, xay), "OR"]

    res = ",".join(sorted(output))

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
