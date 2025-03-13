import sys

input = sys.stdin.readline


def solve(n):
    dp = [0] * (n + 1)

    path = [0] * (n + 1)

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1
        path[i] = i - 1

        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            path[i] = i // 2

        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            path[i] = i // 3

    min_ans = dp[n]

    route = [n]
    while n > 1:
        n = path[n]
        route.append(n)

    return min_ans, route


n = int(input())
ans, route = solve(n)

print(ans)
print(' '.join(map(str, route)))