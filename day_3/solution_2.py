import re

with open("input.txt", "r") as input_file:
    instructions = "".join(input_file.readlines())
    
    valid_mults = re.findall(r"(mul\(\d*,\d*\)|do\(\)|don't\(\))", instructions)
    res = 0
    do = True
    for cmd in valid_mults:
        if cmd == "do()":
            do = True
        elif cmd == "don't()":
            do = False
        elif do:
            a, b = cmd.split(",")
            res += int(a[4:]) * int(b[:-1])
        
    with open("output_2.txt", "w") as output_file:
        output_file.write(str(res))
