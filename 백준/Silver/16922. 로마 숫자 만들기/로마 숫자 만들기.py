import sys

input = sys.stdin.readline


def solve(idx, cnt, total):
    if cnt == N:
        results.add(total)
        return

    for i in range(idx, 4):
        solve(i, cnt + 1, total + nums[i])


N = int(input())

nums = [1, 5, 10, 50]
results = set()

solve(0, 0, 0)  # idx, cnt, total

print(len(results))
