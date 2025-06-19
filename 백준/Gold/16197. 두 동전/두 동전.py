import sys
from collections import deque

input = sys.stdin.readline

'''
하나만 떨어지는 경우만 ok, 2개 다 떨어지면 안됨
x1, y1, x2, y2, cnt 형식으로 deque에 넣어서 문제 풀이
코인을 하나씩 관리하려고 했는데, 그냥 1,2 이런식으로 해서 두 개 다 한번에 하는 방법이 당연한 것 같다
'''


def is_out(x, y):
    # 동전이 나갔는지 여부 체크
    return x < 0 or x >= n or y < 0 or y >= m


def solve():
    visited = set()
    q = deque()
    (x1, y1), (x2, y2) = coins
    q.append((x1, y1, x2, y2, 0))
    visited.add((x1, y1, x2, y2))

    while q:
        x1, y1, x2, y2, cnt = q.popleft()

        if cnt >= 10:
            return -1

        for d in range(4):
            nx1, ny1 = x1 + dx[d], y1 + dy[d]
            nx2, ny2 = x2 + dx[d], y2 + dy[d]

            out1 = is_out(nx1, ny1)
            out2 = is_out(nx2, ny2)

            # 두 동전 중에 하나만 빠지는 경우에만 cnt + 1하여 return
            if out1 and out2:
                continue
            elif out1 or out2:
                return cnt + 1

            # 벽이면 이동 못함
            if not out1 and board[nx1][ny1] == '#':
                nx1, ny1 = x1, y1
            if not out2 and board[nx2][ny2] == '#':
                nx2, ny2 = x2, y2

            # 둘 중 하나만 떨어지지 않았고, 벽이 아닌 위치로 두 개 다 이동한 경우 계속 진행
            if (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                q.append((nx1, ny1, nx2, ny2, cnt + 1))

    return -1


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

coins = []

# 동전 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coins.append((i, j))

print(solve())
