import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

'''
바이러스를 2인 장소에 조합으로 m개 씩 놓으면서 바이러스를 퍼뜨려 보면서 최소 시간을 구해보기
'''


def solve(virus_comb):
    q = deque()
    visited = [[-1] * n for _ in range(n)]

    for x, y in virus_comb:
        q.append((x, y))
        visited[x][y] = 0

    time = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1:
                if visited[i][j] == -1:
                    return float('inf')

                time = max(time, visited[i][j])

    return time


n, m = map(int, input().split())    # n: 크기, m: 바이러스 수
lab = [list(map(int, input().split())) for _ in range(n)]

# 바이러스를 놓을 수 있는 위치를 담기
virus_loc = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_loc.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = float('inf')

# 조합으로 바이러스를 놓을 수 있는 경우의 수를 통해 최소 시간 찾기
for virus_comb in combinations(virus_loc, m):
    tmp_ans = solve(virus_comb)
    ans = min(ans, tmp_ans)

print(ans if ans != float('inf') else -1)
