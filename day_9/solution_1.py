with open("input.txt", "r") as input_file:
    res = 0
    line = input_file.readlines()[0].rstrip()
    data = []
    for i in range(len(line)):
        if i % 2 == 0:
            data.extend([i // 2] * int(line[i]))
        else:
            data.extend([-1] * int(line[i]))

    # Bring stuff to the front, one by one
    l = 0
    r = len(data) - 1
    while True:
        while data[l] != -1:
            l += 1
        while data[r] == -1:
            r -= 1
        if l >= r:
            break
        data[l], data[r] = data[r], data[l]

    checksum = 0
    for i in range(len(data)):
        if data[i] == -1:
            break  # No more data after this point
        checksum += i * data[i]

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(checksum))
