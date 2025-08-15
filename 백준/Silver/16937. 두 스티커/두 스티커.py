import sys
from itertools import combinations

input = sys.stdin.readline


'''
가능한 만큼 붙이는게 아니고 스티커 중에 2개만 골라서 최대값 뽑기
각 스티커의 상태(기본, 기본), (기본, 회전), (회전, 기본), (회전, 회전)의 조합 중에서
가로로 붙이는 경우, 세로로 붙이는 경우를 나눠서 하면 될듯
'''


def solve():
    ans = 0

    for (r1, c1), (r2, c2) in combinations(data, 2):
        for h1, w1 in [(r1, c1), (c1, r1)]:
            for h2, w2 in [(r2, c2), (c2, r2)]:
                # 세로로 나란히 붙이는 경우
                if h1 <= h and h2 <= h and w1 + w2 <= w:
                    ans = max(ans, h1 * w1 + h2 * w2)

                # 가로로 아래쪽으로 붙이는 경우
                if w1 <= w and w2 <= w and h1 + h2 <= h:
                    ans = max(ans, h1 * w1 + h2 * w2)

    return ans


h, w = map(int, input().split())  # h: 높이, w: 너비
n = int(input())  # n: 스티커 개수
data = [list(map(int, input().split())) for _ in range(n)]

print(solve())
