import sys

input = sys.stdin.readline

'''
최소삽입횟수 = N - 가장 긴 팰린드롬 부분 수열 길이
'''


def solve():
    # dp[i][j] = i번 원소부터 j번 원소까지의 부분 수열에서 가장 긴 팰린드롬 부분 수열의 길이
    dp = [[0] * N for _ in range(N)]

    # 길이가 1인 경우(자기 자신은 언제나 팰린드롬)
    for i in range(N):
        dp[i][i] = 1

    # 길이가 2 이상인 경우
    for length in range(2, N+1):
        for i in range(N - length + 1):
            j = i + length - 1
            # 양 끝이 같다면, 해당 길이만큼 가장 긴 펠린드롬이 늘어남
            if nums[i] == nums[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    # i와 j사이인 i+1과 j-1의 팰린드롬 수 + 2
                    dp[i][j] = dp[i+1][j-1] + 2
            # 양 끝이 같지 않다면, i+1부터 j와 i부터 j-1중 더 큰 팰린드롬 수가 됨
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return N - dp[0][N-1]


N = int(input())
nums = list(map(int, input().split()))

print(solve())
