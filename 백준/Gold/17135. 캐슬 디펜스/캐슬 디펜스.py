import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

'''
궁수를 3명을 놓는 방식을 조합으로 배치를 하고
copy로 계속 따로 맵을 만들고 궁수는 (N, col)에 있다고 가정하고 좌표 값으로만 관리하기
'''


def get_target(r, c, enemies):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((r-1, c, 1))   # 궁수를 N행에 있다고 가정하고 하기 때문에, r-1 처리 후 계산 / 가장 가까운 거리 1부터 확인 후 거리를 1씩 늘려감

    while q:
        x, y, dist = q.popleft()
        if dist > D:
            break
        if 0 <= x < N and 0 <= y < M and not visited[x][y]:
            visited[x][y] = True
            if enemies[x][y] == 1:
                return (x, y)
            # 왼쪽, 위, 오른쪽 순서로 보기
            for dx, dy in [(0, -1), (-1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                q.append((nx, ny, dist + 1))

    return None


def solve(curr):
    tmp_map = copy.deepcopy(board)
    cnt = 0

    for _ in range(N):
        targets = set()
        for c in curr:
            target = get_target(N, c, tmp_map)
            if target:
                targets.add(target)

        for x, y in targets:
            if tmp_map[x][y] == 1:
                tmp_map[x][y] = 0
                cnt += 1

        tmp_map.pop()
        tmp_map.insert(0, [0]*M)

    return cnt


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]   # 0: 빈 칸, 1: 적

ans = -float('inf')
# 조합으로 궁수를 배치하는 경우를 돌리기
for case in combinations(range(M), 3):
    ans = max(ans, solve(case))

print(ans)
