import sys

input = sys.stdin.readline


def solve():
    for turn in range(1, 1001):
        for now in range(k):
            x, y, d = horses[now]
            idx = board[x][y].index(now)

            moving = board[x][y][idx:]
            board[x][y] = board[x][y][:idx]

            nx, ny = x + dx[d], y + dy[d]

            # 파랑, 범위 밖일 때: 방향을 뒤집고 해당 방향으로 갈 수 있는지 확인
            if not (0 <= nx < n and 0 <= ny < n) or colors[nx][ny] == 2:
                d = [1, 0, 3, 2][d]

                horses[now][2] = d
                nx, ny = x + dx[d], y + dy[d]

                # 방향을 바꾼 후에도 범위 밖이거나, 파랑이면 제자리에 있기
                if not (0 <= nx < n and 0 <= ny < n) or colors[nx][ny] == 2:
                    board[x][y].extend(moving)
                    continue

            # 빨강: 순서 뒤집기
            if colors[nx][ny] == 1:
                moving.reverse()

            # 흰색: 이동
            for m in moving:
                horses[m][0], horses[m][1] = nx, ny
            board[nx][ny].extend(moving)

            if len(board[nx][ny]) >= 4:
                return turn

    return -1


n, k = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(n)] # 0: 흰, 1: 빨, 2: 파
board = [[[] for _ in range(n)] for _ in range(n)]

horses = []
for i in range(k):
    r, c, hd = map(int, input().split())
    horses.append([r - 1, c - 1, hd - 1])
    board[r - 1][c - 1].append(i)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

print(solve())
