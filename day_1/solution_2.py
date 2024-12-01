with open("input.txt", "r") as input_file:
    a, b = [], []
    for line in input_file.readlines():
        a_item, b_item = map(int, line.split())
        a.append(a_item)
        b.append(b_item)
    a.sort()
    b.sort()

    similarity_score = 0
    for a_item in a:
        print(type(a_item), type(b), type(b.count(a_item)))
        similarity_score += a_item * b.count(a_item)

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(similarity_score))
