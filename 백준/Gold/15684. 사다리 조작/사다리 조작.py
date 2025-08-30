import sys

input = sys.stdin.readline

'''
최대 3개까지 가로선을 추가해보며 i번에서 출발하여 i번으로 갈 수 있는지 확인
'''


def check(board):
    for start in range(1, N+1):
        c = start
        for r in range(1, H+1):
            # 오른쪽으로 이동
            if board[r][c]:
                c += 1
            # 왼쪽으로 이동
            elif c > 1 and board[r][c-1]:
                c -= 1

        if c != start:
            return False

    return True


def solve(idx, added):
    global ans

    if added >= ans or added > 3:
        return

    # 현재 배치로 i에서 i로 돌안다면 갱신
    if check(board):
        ans = min(ans, added)
        return

    # 백트래킹으로 계속 놓아보기
    for i in range(idx, len(candidates)):
        r, c = candidates[i]

        if board[r][c] or (c > 1 and board[r][c-1]) or (c + 1 < N + 1 and board[r][c+1]):
            continue

        board[r][c] = True
        solve(i + 1, added + 1)
        board[r][c] = False


N, M, H = map(int, input().split())
# board[r][c] == True: r번째 줄에서 c+1로 연결하는 가로선이 존재한다는 뜻(True면 놓을 수 없는 곳)
board = [[False] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = True

# 사다리를 놓을 수 있는 위치 미리 뽑아 두기
candidates = []
for r in range(1, H+1):
    for c in range(1, N):
        # 해당 위치에 사다리가 있다면 x
        if board[r][c]:
            continue
        # 해당 위치에서 왼쪽이 True면 사다리 놓을 수 없음
        if c > 1 and board[r][c-1]:
            continue
        # 해당 위치에서 오른쪽이 True면 사다리 놓을 수 없음
        if c + 1 < N + 1 and board[r][c+1]:
            continue
        candidates.append((r, c))

# 답이 가능한 max 범위
ans = 4

# dfs 진행으로 답 찾기
solve(0, 0)

print(ans if ans <= 3 else -1)
