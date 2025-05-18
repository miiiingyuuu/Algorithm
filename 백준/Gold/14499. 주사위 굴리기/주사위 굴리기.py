import sys

input = sys.stdin.readline


def solve(x, y):
    for order in orders:
        nx = x + dx[order]
        ny = y + dy[order]

        if not(0 <= nx < n and 0 <= ny < m):
            continue

        # 주사위: 윗, 앞, 동, 서, 뒤, 아래
        # 앞, 뒤 빼고 움직임
        if order == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif order == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        # 동, 서 빼고 움직임
        elif order == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif order == 4:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        # 이동한 칸이 0이면 주사위 바닥면이 쓰여있는 수가 되고, 0이 아니면 칸에 있는 수가 주사위 바닥면에 복사 후, 칸에 있는 수는 0이 됨
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0

        print(dice[0])
        x, y = nx, ny


n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]   # 윗, 앞, 동, 서, 뒤, 아래

# order가 1부터 시작해서 0 인덱싱 (동, 서, 북, 남)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

solve(x, y)