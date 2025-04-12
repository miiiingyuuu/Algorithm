import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def solve():
    room[0][0] = 1
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for a, b in switches[(x, y)]:
            if not room[a][b]:
                room[a][b] = 1
                for i in range(4):
                    na = a + dx[i]
                    nb = b + dy[i]
                    if 0 <= na < n and 0 <= nb < n and visited[na][nb]:
                        q.append((a, b))
                        visited[a][b] = True
                        break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and room[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


n, m = map(int, input().split())
switches = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switches[(x-1, y-1)].append((a-1, b-1))

room = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

solve()

result = sum([row.count(1) for row in room])
print(result)