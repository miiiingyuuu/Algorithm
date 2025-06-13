import sys
from collections import deque

input = sys.stdin.readline

'''
bfs로 방문하지 않은 곳의 벽을 깨면서 이동하며 벽을 몇개 깼는지 확인
visited 그래프에 -1로 채워서 시작 부분은 0으로 초기화하여 벽이 아닌 곳을 갈때는 이전 벽의 개수로 바꾸고, 벽을 부숴서 간다면 +1 처리
그런데 벽을 최소로 부수는 경우니까, 0인 곳을 가는게 최우선으로 해서 appendleft, 벽을 부쉈을 경우에는 제일 뒤로 append
'''


def solve():
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 0

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    # 빈 방이면 벽 부수지 않고 이전에 부쉈던 벽 개수대로 처리 (앞에 넣기)
                    if board[nx][ny] == '0':
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    # 벽이면 부수기 처리 (뒤에 넣기)
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

    return visited[n-1][m-1]


m, n = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(solve())
