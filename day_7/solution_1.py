from functools import lru_cache


@lru_cache
def could_be_true(desired_result, values, current_result=0, value_idx=0):
    if value_idx == len(values):
        return current_result == desired_result

    if value_idx == 0:
        return could_be_true(desired_result, values, values[0], 1)

    if could_be_true(
        desired_result, values, values[value_idx] + current_result, value_idx + 1
    ) or could_be_true(
        desired_result, values, values[value_idx] * current_result, value_idx + 1
    ):
        return True

    return False


with open("input.txt", "r") as input_file:
    res = 0
    for line in input_file.readlines():
        a, b = line.split(":")
        desired_result = int(a)
        values = tuple(map(int, b.split()))
        if could_be_true(desired_result, values):
            res += desired_result

    with open("output_1.txt", "w") as output_file:
        output_file.write(str(res))
