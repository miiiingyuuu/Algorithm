import sys

input = sys.stdin.readline


def solve():
    min_h = hills[0]
    max_h = hills[-1]

    if max_h - min_h <= 17:
        return 0

    min_cost = float('inf')

    for i in range(min_h, max_h - 16):
        max_p = i + 17
        cost = 0

        for h in hills:
            if h < i:
                cost += (i - h) ** 2
            elif h > max_p:
                cost += (h - max_p) ** 2

        min_cost = min(min_cost, cost)

    return min_cost


n = int(input())
hills = [int(input()) for _ in range(n)]
hills.sort()

print(solve())