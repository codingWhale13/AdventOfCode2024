with open("input.txt", "r") as input_file:
    reports = []
    for line in input_file.readlines():
        report = [int(i) for i in line.split()]
        reports.append(report)

    safe_report_count = 0
    for report in reports:
        current = report[0]
        diff_okay = True
        up_okay = True
        down_okay = True
        for i in range(1, len(report)):
            if not report[i] > current:
                up_okay = False
            if not report[i] < current:
                down_okay = False
            if not 1 <= abs(report[i] - current) <= 3:
                diff_okay = False

            current = report[i]

        if diff_okay and (up_okay or down_okay):
            safe_report_count += 1

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(safe_report_count))
