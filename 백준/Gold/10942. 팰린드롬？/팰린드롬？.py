import sys

input = sys.stdin.readline


def solve():
    dp = [[0] * n for _ in range(n)]

    # 범위가 1인 경우
    for i in range(n):
        dp[i][i] = 1

    # 범위가 2인 경우
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1

    # 범위가 3이상인 경우
    for i in range(3, n + 1):
        for j in range(n - i + 1):
            k = i + j - 1
            if nums[j] == nums[k] and dp[j+1][k-1]:
                dp[j][k] = 1
                
    results = []
    for s, e in questions:
        results.append(dp[s-1][e-1])

    return results


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
questions = []
for _ in range(m):
    s, e = map(int, input().split())
    questions.append((s, e))

results = solve()

for result in results:
    print(result)