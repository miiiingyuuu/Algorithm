import sys

input = sys.stdin.readline


'''
N이 주어졌을 때, 가능한 점수 중 최대값
-> 팔굽 횟수가 누적으로 늘어나느 것이니까 여러 방법으로 답이 나올 수도 있었음, 그 중에서 최대값을 뽑아야 함
'''


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())    # N: 팔굽 횟수, M: 점수 갯수
    scores = list(map(int, input().split()))    # 점수 당 팔굽 1번

    # dp[i]: 팔굽횟수가 i일때 얻을 수 있는 최대 점수
    dp = [set() for _ in range(N+1)]
    dp[0].add(0)

    # 팔굽 횟수
    for i in range(N+1):
        # 해당 팔굽 횟수 진행할 수 없으면 넘어가기
        if not dp[i]:
            continue

        for curr_score in dp[i]:
            for s in scores:
                # 새로운 총 득점(= 가능한 다음 총 팔굽 횟수)
                new_score = curr_score + s

                # 갱신된 총 팔굽 횟수
                new_push_ups = i + new_score

                if new_push_ups <= N:
                    dp[new_push_ups].add(new_score)

    if dp[N]:
        print(max(dp[N]))
    else:
        print(-1)
