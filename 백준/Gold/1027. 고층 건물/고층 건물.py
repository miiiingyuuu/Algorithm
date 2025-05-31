import sys

input = sys.stdin.readline

'''
i번째에서 좌우로 나눠서 기울기를 계산했을때, 기울기가 더 커진다면 볼 수 있는 것
'''


def solve(idx):
    cnt = 0

    # 왼쪽 탐색(기울기가 작아질수록 볼 수 있음)
    min_slope = float('inf')
    for j in range(idx - 1, -1, -1):
        slope = (h[idx] - h[j]) / (idx - j)
        if slope < min_slope:
            min_slope = slope
            cnt += 1

    # 오른쪽 탐색(기울기가 커질수록 볼 수 있음)
    max_slope = -float('inf')
    for k in range(idx + 1, n):
        slope = (h[idx] - h[k]) / (idx - k)
        if slope > max_slope:
            max_slope = slope
            cnt += 1

    return cnt


n = int(input())
h = list(map(int, input().split()))

result = 0
for i in range(n):
    result = max(result, solve(i))

print(result)