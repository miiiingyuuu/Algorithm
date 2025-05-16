import sys

input = sys.stdin.readline


def solve():
    dp = [[0] * (w+1) for _ in range(t+1)]  # t초까지, w번 이동했을 때 받을 수 있는 최대 자두 수

    # 시간
    for i in range(1, t+1):
        # 움직이는 횟수
        for j in range(w+1):
            # 이동을 하지 않은 경우는 무조건 1번 나무 아래
            if j == 0:
                if drop_tree[i] == 1:
                    dp[i][j] = dp[i-1][j] + 1
                else:
                    dp[i][j] = dp[i-1][j]
            # 이동 횟수가 짝수면 1번, 홀수면 2번 나무
            else:
                if drop_tree[i] == (j % 2) + 1:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

    return max(dp[t])


t, w = map(int, input().split())
drop_tree = [0] + [int(input().strip()) for _ in range(t)]

print(solve())