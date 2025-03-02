import sys

input = sys.stdin.readline


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0

while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1

    # 청소되지 않은 빈 칸이 있는지 확인
    uncleaned = False
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
            uncleaned = True
            break

    # 청소되지 않은 빈 칸이 없는 경우
    if not uncleaned:
        # 후진 방향 설정
        back_d = (d+2) % 4
        back_r = r + dr[back_d]
        back_c = c + dc[back_d]

        # 후진 할 수 있는지 체크 후 방향 변경 후 이동
        if 0 <= back_r < N and 0 <= back_c < M and board[back_r][back_c] != 1:
            r, c = back_r, back_c
        # 후진 할 수 없다면 작동 멈춤
        else:
            break

    # 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반시계 방향으로 90도 회전 설정
        d = (d+3)%4
        forward_r = r + dr[d]
        forward_c = c + dc[d]

        # 청소되지 않은 빈칸인지 확인 후 방향 변경 후, 이동
        if 0 <= forward_r < N and 0 <= forward_c < M and board[forward_r][forward_c] == 0:
            r, c = forward_r, forward_c

print(cnt)