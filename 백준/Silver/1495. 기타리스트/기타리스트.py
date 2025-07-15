import sys

input = sys.stdin.readline

'''
dp[i][j] = i번째 곡을 연주 할때 가능한 볼륨 저장 j(0 ~ m)
해당하는 볼륨이 가능할 경우 1로 표시
'''


def solve():
    dp = [[0] * (m+1) for _ in range(n+1)]

    # 볼륨 s에서 시작
    dp[0][s] = 1

    # i번째 곡을 연주
    for i in range(n):
        for j in range(m+1):
            if dp[i][j] == 1:
                if j + volumes[i] <= m:
                    dp[i+1][j+volumes[i]] = 1
                if 0 <= j - volumes[i]:
                    dp[i+1][j-volumes[i]] = 1

    return dp[n]


n, s, m = map(int, input().split())    # n: 곡의 개수, s: 시작 볼륨, m: 볼륨 max 값
volumes = list(map(int, input().split()))

result = solve()

# n번째 곡에서 해당하는 볼륨이 있다면(1이 있으면) 해당 r 출력 없다면 ans의 변화가 없으므로 ans 출력
ans = -1
for r in range(m, -1, -1):
    if result[r] == 1:
        ans = r
        break

print(ans)
