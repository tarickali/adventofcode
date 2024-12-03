from collections import Counter


def solution():
    file_name = "input.txt"

    left_list = []
    right_list = []
    with open(file_name) as f:
        for line in f.readlines():
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

    right_counts = Counter(right_list)

    total_similarity = 0
    for n in left_list:
        total_similarity += n * right_counts.get(n, 0)

    return total_similarity


if __name__ == "__main__":
    sol = solution()

    print(sol)
