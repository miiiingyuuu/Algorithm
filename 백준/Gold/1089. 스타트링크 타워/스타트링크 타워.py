import sys

input = sys.stdin.readline

digits = [
    ["###", "#.#", "#.#", "#.#", "###"],  # 0
    ["..#", "..#", "..#", "..#", "..#"],  # 1
    ["###", "..#", "###", "#..", "###"],  # 2
    ["###", "..#", "###", "..#", "###"],  # 3
    ["#.#", "#.#", "###", "..#", "..#"],  # 4
    ["###", "#..", "###", "..#", "###"],  # 5
    ["###", "#..", "###", "#.#", "###"],  # 6
    ["###", "..#", "..#", "..#", "..#"],  # 7
    ["###", "#.#", "###", "#.#", "###"],  # 8
    ["###", "#.#", "###", "..#", "###"],  # 9
]


def match(pattern, num):
    for r in range(5):
        for c in range(3):
            if pattern[r][c] == '#' and digits[num][r][c] == '.':
                return False
    return True


def solve():
    candidates = []

    for k in range(N):
        pattern = [row[4 * k:4 * k + 3] for row in board]
        possible = [d for d in range(10) if match(pattern, d)]

        if not possible:
            return -1
        candidates.append(possible)

    # 전체 경우의 수
    total_count = 1
    for c in candidates:
        total_count *= len(c)

    total_sum = 0
    for i in range(N):
        digit_sum = sum(candidates[i])
        digit_count = len(candidates[i])

        # 다른 자리수들의 경우의 수
        other_count = total_count // digit_count

        place_value = 10 ** (N - 1 - i)
        total_sum += digit_sum * place_value * other_count

    return total_sum / total_count


N = int(input())
board = [input().strip() for _ in range(5)]

print(solve())
