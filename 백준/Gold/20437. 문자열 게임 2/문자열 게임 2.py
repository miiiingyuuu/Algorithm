import sys

input = sys.stdin.readline


def solve():
    words = set(w)

    min_ans = float('inf')
    max_ans = -1

    for word in words:
        positions = [idx for idx, c in enumerate(w) if c == word]

        if len(positions) < k:
            continue

        # 3번 조건
        for j in range(len(positions) - k + 1):
            length = positions[j+k-1] - positions[j] + 1
            min_ans = min(min_ans, length)

        # 4번 조건
        for j in range(len(positions) - k + 1):
            start = positions[j]
            end = positions[j+k-1]
            length = end - start + 1
            max_ans = max(max_ans, length)

    if min_ans == float('inf'):
        min_ans = -1

    return min_ans, max_ans


t = int(input())
for tc in range(t):
    w = input()
    k = int(input())

    min_len, max_len = solve()

    if min_len == -1:
        print(-1)
    else:
        print(min_len, max_len)