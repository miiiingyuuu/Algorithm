import sys

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve(x, y):
    global ans

    end = min(N, M)

    for e in range(1, end+1):
        found = False
        for d in range(4):
            nx = x + (dx[d] * e)
            ny = y + (dy[d] * e)
            if not (0 <= nx < N and 0 <= ny < M):
                break

            if board[nx][ny] == '*':
                if d == 3:
                    found = True
            else:
                break

        if not found:
            break
        else:
            ans.append((x + 1, y + 1, e))


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

ans = []

tar = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            tar += 1
            solve(i, j)
            
check = set()

for x, y, e, in ans:
    if (x, y) not in check:
        check.add((x, y))

    for ei in range(1, e+1):
        for cd in range(4):
            cx = x + (dx[cd] * ei)
            cy = y + (dy[cd] * ei)
            if (cx, cy) not in check:
                check.add((cx, cy))


if len(ans) > 0 and len(check) == tar:
    print(len(ans))
    for a in ans:
        print(*a)
else:
    print(-1)
