import sys

input = sys.stdin.readline


N = int(input())
desks = [list(map(int, input().split())) for _ in range(N)]

# dp[g] = 직전 책상까지의 연속 길이
dp = [0] * 6
max_val = 0
ans = 0

for a, b in desks:
    new_dp = [0] * 6
    for g in range(1, 6):
        if g == a or g == b:
            new_dp[g] = dp[g] + 1
            # 그레이드가 작은 경우가 답
            if new_dp[g] > max_val or (new_dp[g] == max_val and g < ans):
                max_val = new_dp[g]
                ans = g

        else:
            new_dp[g] = 0

    dp = new_dp

print(max_val, ans)
