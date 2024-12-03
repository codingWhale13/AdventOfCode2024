import re

with open("input.txt", "r") as input_file:
    instructions = "".join(input_file.readlines())
    
    valid_mults = re.findall(r"(mul\(\d*,\d*\))", instructions)
    res = 0
    for mult in valid_mults:
        a, b = mult.split(",")
        res += int(a[4:]) * int(b[:-1])
        
    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
