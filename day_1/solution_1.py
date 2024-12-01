with open("input.txt", "r") as input_file:
    a, b = [], []
    for line in input_file.readlines():
        a_item, b_item = map(int, line.split())
        a.append(a_item)
        b.append(b_item)
    a.sort()
    b.sort()

    diff = 0
    for a_item, b_item in zip(a, b):
        diff += abs(a_item - b_item)

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(diff))
