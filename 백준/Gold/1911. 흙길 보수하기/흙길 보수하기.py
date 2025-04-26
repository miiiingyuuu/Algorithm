import sys
import math
input = sys.stdin.readline


def solve():
    ans = 0
    pos = 0

    for start, end in pools:
        if pos < start:
            pos = start

        if pos < end:
            length = end - pos
            cnt = math.ceil(length / l)
            ans += cnt
            pos += cnt * l

    return ans


n, l = map(int, input().split())    # n: 웅덩이 갯수, l: l길이의 널빤지
pools = [list(map(int, input().split())) for _ in range(n)]
pools.sort()

print(solve())