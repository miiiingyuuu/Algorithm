import sys

input = sys.stdin.readline


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]   # lst[i][j]: i: 걸리는 일 수, j:이익

dp = [0] * (n+1)    # 각 날에 걸쳐서 얻을 수 있는 이득을 저장하는 dp

max_val = 0
for i in range(n):
    # 그 날까지 얻을 수 있는 최대 이익
    max_val = max(max_val, dp[i])
    # 퇴사일을 넘긴다면 일 할 수 없음
    if i + lst[i][0] > n:
        continue

    dp[i+lst[i][0]] = max(dp[i+lst[i][0]], max_val + lst[i][1])

print(max(dp))