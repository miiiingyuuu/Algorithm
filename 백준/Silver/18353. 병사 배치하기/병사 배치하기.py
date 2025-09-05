import sys

input = sys.stdin.readline

'''
남은 병사가 최대가 되기 위해 몇 명을 제외시켜야 하는가?
N - 가장 긴 감소하는 부분 수열의 길이를 하면 답이 나오겠네
'''


def solve():
    # dp[i]: i번째 원소를 마지막으로 하는 가장 긴 감소하는 부분 수열의 길이
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if datas[j] > datas[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    longest = max(dp)
    return N - longest


N = int(input())
datas = list(map(int, input().split()))

print(solve())
