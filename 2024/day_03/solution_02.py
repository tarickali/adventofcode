import re


def solution():
    file_name = "input.txt"

    memory = ""
    with open(file_name) as f:
        memory = f.read()

    regex = re.compile("(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))")
    matches = regex.findall(memory)

    enable = True
    total = 0
    for instruction, x, y in matches:
        if instruction == "do()":
            enable = True
        elif instruction == "don't()":
            enable = False
        else:  # mul
            if enable:
                total += int(x) * int(y)

    return total


if __name__ == "__main__":
    sol = solution()
    print(sol)
