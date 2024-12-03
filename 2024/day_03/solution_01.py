import re


def solution():
    file_name = "input.txt"

    memory = ""
    with open(file_name) as f:
        memory = f.read()

    regex = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    matches = regex.findall(memory)

    total = 0
    for x, y in matches:
        total += int(x) * int(y)

    return total


if __name__ == "__main__":
    sol = solution()
    print(sol)
