import sys

input = sys.stdin.readline


'''
사용하는 힘: (j-i) * (1+|Ai - Aj|)
'''


def solve():
    dp = [False] * N    # dp[i]: i번쨰 돌을 갈 수 있는지 체크

    dp[0] = True

    for i in range(N):
        # 해당하는 돌부터 점프가 가능한지 확인해야 하므로 dp[i]가 True인 곳에서 갈 수 있는지 확인
        if not dp[i]:
            continue

        # 해당하는 에너지로 dp[j] 돌을 갈 수 있는지 확인, 해당 위치에서 못가는 에너지면 바로 break
        for j in range(i+1, N):
            energy = (j - i) * (1 + abs(A[i] - A[j]))
            if energy <= K:
                dp[j] = True

    return "YES" if dp[N-1] else "NO"


N, K = map(int, input().split())
A = list(map(int, input().split()))

print(solve())
