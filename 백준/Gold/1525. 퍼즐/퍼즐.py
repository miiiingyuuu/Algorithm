import sys
from collections import deque

input = sys.stdin.readline


def solve(r, c, start):
    visited = set()
    q = deque()

    visited.add(start)
    q.append((r, c, start, 0))     # r, c(좌표), 현재상태, cnt

    while q:
        x, y, now, cnt = q.popleft()

        if now == "123456780":
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 3 and 0 <= ny < 3:
                pos = x * 3 + y
                n_pos = nx * 3 + ny

                now_lst = list(now)
                now_lst[pos], now_lst[n_pos] = now_lst[n_pos], now_lst[pos]
                new_state = "".join(now_lst)

                if new_state not in visited:
                    visited.add(new_state)
                    q.append((nx, ny, new_state, cnt + 1))

    return -1


board = [list(map(int, input().split())) for _ in range(3)]

lst = []
for i in range(3):
    lst.extend(board[i])

start = "".join(map(str, lst))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            print(solve(i, j, start))
            break
