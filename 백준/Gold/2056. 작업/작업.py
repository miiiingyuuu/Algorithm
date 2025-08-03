import sys

input = sys.stdin.readline


'''
dp[i] = i번 작업을 완료하는 데 걸리는 최소 시간(현재 작업 + 선행 작업의 완료 가능 시간(max값))
데이터를 한 줄씩 받아와서 선행 작업의 최대값과 비교하며 값 갱신하기
'''


def solve(curr, line):
    curr_time = line[0]

    max_time = 0

    # 선행 작업이 있는지 확인
    if line[1] > 0:
        priorities = line[2:]
        for priority in priorities:
            # 선행 작업들의 완료 시간 중 최댓값을 찾기
            if dp[priority] > max_time:
                max_time = dp[priority]

    # dp[i] = 현재 작업의 완료 시간 + 가장 늦게 끝나는 선행 작업의 완료 시간
    dp[curr] = max_time + curr_time


N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
    datas = list(map(int, input().split()))
    solve(i, datas)

print(max(dp))