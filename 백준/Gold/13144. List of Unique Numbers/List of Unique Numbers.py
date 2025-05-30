import sys

input = sys.stdin.readline


def solve():
    seen = set()
    start, end = 0, 0
    ans = 0

    while start < n:
        while end < n and sequence[end] not in seen:
            seen.add(sequence[end])
            end += 1
        ans += end - start
        seen.remove(sequence[start])
        start += 1

    return ans


n = int(input())
sequence = list(map(int, input().split()))

print(solve())