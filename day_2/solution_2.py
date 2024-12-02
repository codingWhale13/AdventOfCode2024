with open("input.txt", "r") as input_file:
    reports = []
    for line in input_file.readlines():
        report = [int(i) for i in line.split()]
        reports.append(report)

    safe_report_count = 0
    for og_report in reports:
        for skip in range(-1, len(og_report)):  # -1 -> skip none
            report = [og_report[i] for i in range(len(og_report)) if i != skip]

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
                break

    with open("output_2.txt", "w") as output_file:
        output_file.write(str(safe_report_count))
