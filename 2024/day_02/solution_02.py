def is_safe(report: list[int]) -> bool:
    if len(report) <= 1:
        return True
    if len(report) == 2 and 1 <= abs(report[0] - report[1]) <= 3:
        return True

    is_ascending = report[0] < report[1]

    for i in range(len(report) - 1):
        x = report[i]
        y = report[i + 1]

        if not (
            1 <= abs(x - y) <= 3
            and ((is_ascending and x < y) or (not is_ascending and x > y))
        ):
            return False
    return True


def solution():
    file_name = "input.txt"

    reports = []
    with open(file_name) as f:
        for line in f.readlines():
            reports.append([int(x) for x in line.split()])

    total_safe = 0
    for report in reports:
        if is_safe(report):
            total_safe += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i + 1 :]):
                    total_safe += 1
                    break

    return total_safe


if __name__ == "__main__":
    sol = solution()
    print(sol)
