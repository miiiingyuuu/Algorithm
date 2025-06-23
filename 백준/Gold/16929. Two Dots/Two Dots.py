import sys

input = sys.stdin.readline

'''
dfs를 도는데... 1. n * m 범위 안에 있다.
2. 범위 안에 있는 애들 중에 알파벳이 같고, 방문하지 않은 곳을 방문한다.
3. 만약에 같은 알파벳인데 범위 안에 있고 모두 방문을 했고, 현재 경로에서 이전 칸과 두 칸 이상 떨어진 경우라면 사이클 발생
4. depth >= 4 이상이 되어야 조건 만족
'''


def solve(x, y, from_x, from_y, color, depth):
    if visited[x][y] and depth >= 4:
        return True

    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == color:
            # 방금 왔던 곳은 제외
            if nx == from_x and ny == from_y:
                continue

            if visited[nx][ny]:
                if depth >= 4:
                    return True
                continue

            if solve(nx, ny, x, y, color, depth + 1):
                return True

    return False


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if solve(i, j, -1, -1, board[i][j], 1):
                print("Yes")
                exit()

print("No")
