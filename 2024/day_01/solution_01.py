def solution():
    file_name = "input.txt"

    left_list = []
    right_list = []
    with open(file_name) as f:
        for line in f.readlines():
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    total_distance = 0
    for l, r in zip(left_list, right_list):
        total_distance += abs(l - r)

    return total_distance


if __name__ == "__main__":
    sol = solution()
    print(sol)
