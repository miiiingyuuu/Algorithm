import sys

input = sys.stdin.readline


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


# 2개 이상인 경우 질량, 속력, 방향 재조정
def new_fireballs_move(board):
    new_fireballs = []
    for r in range(N):
        for c in range(N):
            if not board[r][c]:
                continue

            # 하나인 경우
            if len(board[r][c]) == 1:
                m, s, d = board[r][c][0]
                new_fireballs.append((r, c, m, s, d))
            # 둘 이상인 경우
            else:
                sum_m = sum(x[0] for x in board[r][c])
                sum_s = sum(x[1] for x in board[r][c])
                cnt = len(board[r][c])

                new_m = sum_m // 5
                if new_m == 0:
                    continue

                new_s = sum_s // cnt
                dirs = [x[2] % 2 for x in board[r][c]]  # 홀짝 체크
                if all(d == dirs[0] for d in dirs):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                for nd in new_dirs:
                    new_fireballs.append((r, c, new_m, new_s, nd))

    return new_fireballs


# 파이어볼 이동
def fireballs_move(fireballs):
    board = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        board[nr][nc].append((m, s, d))

    return board


def solve(fireballs):
    for _ in range(K):
        board = fireballs_move(fireballs)
        fireballs = new_fireballs_move(board)

    return sum(m for _, _, m, _, _ in fireballs)


N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())   # m: 질량, s: 속력 d: 방향,
    fireballs.append((r-1, c-1, m, s, d))

print(solve(fireballs))
