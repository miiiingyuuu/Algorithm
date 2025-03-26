import sys

input = sys.stdin.readline


def solve():
    stack = []
    ans = [0] * n

    for i in range(n):
        while stack and stack[-1][1] < h[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1][0] + 1

        stack.append((i, h[i]))

    return ans


n = int(input())
h = list(map(int, input().split()))

result = solve()
print(*result)