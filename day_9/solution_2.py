with open("input.txt", "r") as input_file:
    res = 0
    line = input_file.readlines()[0].rstrip()
    data = []
    for i in range(len(line)):
        if i % 2 == 0:
            data.extend([i // 2] * int(line[i]))
        else:
            data.extend([-1] * int(line[i]))

    # Bring stuff to the front, block by block
    r = len(data) - 1
    while r >= 0:
        # Get ready to process next block
        while data[r] == -1:
            r -= 1
            if r < 0:
                break
        block_size = 0
        r2 = r
        while data[r2] == data[r]:
            block_size += 1
            r2 -= 1

        # Try out all free spaces from left to right
        l = 0
        while True:
            while data[l] != -1:
                l += 1
            if l >= r:
                r -= block_size  # Couldn't move block, move on to next one
                break

            free_contiguous = 0
            l2 = l
            while data[l2] == -1:
                free_contiguous += 1
                l2 += 1

            if block_size <= free_contiguous:
                for _ in range(block_size):
                    data[l], data[r] = data[r], data[l]
                    l += 1
                    r -= 1
                break

            # Move on to next block so that l can start looking for next free spot again
            while data[l] == -1:
                l += 1

    checksum = 0
    for i in range(len(data)):
        if data[i] != -1:
            checksum += i * data[i]

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(checksum))
