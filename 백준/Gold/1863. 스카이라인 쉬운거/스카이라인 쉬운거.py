import sys

input = sys.stdin.readline


def solve():
    ans = 0
    buildings = []

    for x, y in h:
        # 현재 높이보다 큰 건물들은 카운팅이 끝났으니 제거
        while buildings and buildings[-1] > y:
            buildings.pop()

        # 같은 높이면 패스, 새로운 높이면 카운팅 증가
        if not buildings or buildings[-1] < y:
            buildings.append(y)
            if y != 0:
                ans += 1

    return ans


n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]

print(solve())