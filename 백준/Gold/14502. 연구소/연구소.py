import sys
import copy
from collections import deque

input = sys.stdin.readline


def solve(n, m, lab):
    def spread_virus(tmp_lab):
        visited = [[False] * m for _ in range(n)]
        q = deque()

        for i in range(N):
            for j in range(M):
                if tmp_lab[i][j] == 2:
                    q.append((i, j))
                    visited[i][j] = True

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if tmp_lab[nx][ny] == 0 and not visited[nx][ny]:
                        tmp_lab[nx][ny] = 2
                        visited[nx][ny] = True
                        q.append((nx, ny))

        safe_cnt = 0
        for i in range(n):
            for j in range(m):
                if tmp_lab[i][j] == 0:
                    safe_cnt += 1
        return safe_cnt

    def build_walls(cnt, x, y):
        nonlocal ans

        if cnt == 3:
            tmp_lab = copy.deepcopy(lab)
            tmp_ans = spread_virus(tmp_lab)
            ans = max(ans, tmp_ans)
            return

        for i in range(x, n):
            start_j = y if i == x else 0
            for j in range(start_j, m):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    build_walls(cnt + 1, i, j + 1)
                    lab[i][j] = 0

    ans = 0
    build_walls(0, 0, 0)
    return ans


N, M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]

result = solve(N, M, laboratory)
print(result)