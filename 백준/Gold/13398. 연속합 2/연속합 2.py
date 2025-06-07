import sys

input = sys.stdin.readline
'''
수열 중에 최소값이 음수라면 안더하는 것이 최대값을 구하는데 용이하지 않을까? -> 근데 무조건 100% 그렇다고 확정은 못함
중간에 음수가 많이 포함되어 있으면, 음수끼리의 합은 무조건 최소가 되기 때문 수열의 합이 음수가 되는 순간에는 다음거부터 다시 더하는게 좋을 수 있음
그래서 그냥 수 제거 없이 하는 경우와 수 제거를 하고 할 수 있는 경우를 2가지로 나눠서 그 중에서 최댓값 출력하는게 맞다.
'''


def solve():
    dp1 = [0] * n  # 수 제거 없이 최대 연속합
    dp2 = [0] * n  # 수 하나 제거 후 최대 연속합

    dp1[0] = nums[0]
    dp2[0] = nums[0]
    ans = nums[0]

    for i in range(1, n):
        dp1[i] = max(dp1[i-1] + nums[i], nums[i])   # 이전 누적합과 현재값 비교
        dp2[i] = max(dp2[i-1] + nums[i], dp1[i-1])  # 이전 누적합과 지금 제거하는 경우 값 비교
        ans = max(ans, dp1[i], dp2[i])  # 매번 ans를 갱신하며 max 값 찾기

    return ans


n = int(input())
nums = list(map(int, input().split()))

print(solve())