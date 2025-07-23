import sys

input = sys.stdin.readline


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve():
    total_dist = 0
    for i in range(1, n):
        total_dist += distance(points[i-1], points[i])

    # 한 지점을 건너뛰었을 때 최대로 절약할 수 있는 거리 계산
    max_val = 0
    for i in range(1, n-1):
        prev = points[i-1]
        now = points[i]
        nxt = points[i+1]

        skip_dist = distance(prev, now) + distance(now, nxt)
        direct_dist = distance(prev, nxt)
        tmp_val = skip_dist - direct_dist
        max_val = max(max_val, tmp_val)

    return total_dist - max_val


n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

print(solve())
