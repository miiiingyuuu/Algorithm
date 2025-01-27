import sys
input = sys.stdin.readline

# N x N 크기의 보드를 입력받음
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# dp[상태][행][열] 형태의 3차원 DP 배열
# 상태: 0(가로), 1(대각선), 2(세로)
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

# 초기 파이프 위치(1,1)-(1,2)를 가로 방향으로 설정
dp[0][0][1] = 1

# 첫 행에서 가로로만 이동 가능한 경우 처리
for i in range(2, n):
   if arr[0][i] == 0:
       dp[0][0][i] = dp[0][0][i-1]

# 나머지 보드 탐색
for k in range(1, n):
   for l in range(1, n):
       # 대각선 이동이 가능한 경우
       if arr[k][l] == 0 and arr[k][l-1] == 0 and arr[k-1][l] == 0:
           dp[1][k][l] = dp[0][k-1][l-1] + dp[1][k-1][l-1] + dp[2][k-1][l-1]

       # 가로, 세로 이동이 가능한 경우
       if arr[k][l] == 0:
           dp[0][k][l] = dp[0][k][l-1] + dp[1][k][l-1]  # 가로 이동
           dp[2][k][l] = dp[2][k-1][l] + dp[1][k-1][l]  # 세로 이동

# (N,N)에 도달하는 모든 경우의 수 합산
print(sum(dp[i][n-1][n-1] for i in range(3)))