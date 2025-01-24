# 0/1 배낭 문제를 해결하는 다이나믹 프로그래밍 코드

# 입력 처리: N(물건 개수), K(배낭 용량) 
N, K = map(int, input().split())

# N개의 물건에 대한 [무게, 가치] 정보 입력
mer = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i번째 물건까지 고려했을 때, 용량 j에서의 최대 가치
dp = [[0]*(K+1) for _ in range(N+1)]

# 각 물건과 용량에 대해 최적의 선택 계산
for i in range(1, N+1):
   for j in range(1, K+1):
       # 현재 물건을 넣을 수 있는 경우
       if j >= mer[i-1][0]:
           # max(현재 물건을 넣는 경우, 넣지 않는 경우)
           dp[i][j] = max(mer[i-1][1] + dp[i-1][j-mer[i-1][0]], dp[i-1][j])
       # 현재 물건을 넣을 수 없는 경우
       else:
           dp[i][j] = dp[i-1][j]

# 최종 결과 출력: N개의 물건을 고려했을 때 용량 K에서의 최대 가치
print(dp[N][K])