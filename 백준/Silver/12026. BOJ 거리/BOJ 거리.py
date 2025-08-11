import sys

input = sys.stdin.readline

'''
점프할 때는 k*k만큼의 에너지 사용
'''


def solve():
    # dp[i] i번째에 올 수 있는 최소 비용
    dp = [float('inf')] * N
    dp[0] = 0

    order = {
        'B': 'O',
        'O': 'J',
        'J': 'B',
    }

    for i in range(N):
        if dp[i] == -1:
            continue

        # 해당 블록에서 갈 수 있는 블록에 모두 에너지 사용량을 기록해두고, 거기서 최소값을 갱신하기
        for j in range(i+1, N):
            if blocks[j] == order[blocks[i]]:
                cost = (i - j)**2
                dp[j] = min(dp[j], dp[i] + cost)

    return dp[N-1] if dp[N-1] != float('inf') else -1


N = int(input())
blocks = input().strip()

print(solve())
