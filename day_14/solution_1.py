with open("input.txt", "r") as input_file:
    pos = []
    vel = []
    for line in input_file.readlines():
        a, b = line.split()
        x_str, y_str = a.split(",")
        xv_str, yv_str = b.split(",")

        pos.append((int(x_str[2:]), int(y_str)))
        vel.append((int(xv_str[2:]), int(yv_str)))

    h, w = 103, 101
    step_count = 100

    robot_count = len(pos)
    for i in range(robot_count):
        x, y = pos[i]
        vx, vy = vel[i]
        pos[i] = (
            (x + vx * step_count + w * step_count) % w,
            (y + vy * step_count + h * step_count) % h,
        )

    quadrant_counts = [0, 0, 0, 0]
    for p in pos:
        x, y = p
        if x < w // 2 and y < h // 2:
            quadrant_counts[0] += 1
        elif x > w // 2 and y < h // 2:
            quadrant_counts[1] += 1
        elif x < w // 2 and y > h // 2:
            quadrant_counts[2] += 1
        elif x > w // 2 and y > h // 2:
            quadrant_counts[3] += 1
    res = (
        quadrant_counts[0]
        * quadrant_counts[1]
        * quadrant_counts[2]
        * quadrant_counts[3]
    )

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
