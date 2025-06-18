import sys

input = sys.stdin.readline

'''
0의 위치를 미리 blanks라는 리스트에 저장을 해두고 blanks의 길이 만큼 index가 백트래킹을 통해 완료
스도쿠 게임 룰대로 가로, 세로, 3x3을 체크
'''


def is_valid(x, y, num):
    # 행 체크
    if num in board[x]:
        return False

    # 열 체크
    for i in range(9):
        if board[i][y] == num:
            return False

    # 3x3 체크
    nx, ny = 3 * (x // 3), 3 * (y // 3)
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if board[i][j] == num:
                return False

    return True


def solve(idx):
    if idx == len(blanks):
        for row in board:
            print(' '.join(map(str, row)))
        sys.exit()

    x, y = blanks[idx]
    for num in range(1, 10):
        if is_valid(x, y, num):
            board[x][y] = num
            solve(idx + 1)
            board[x][y] = 0


board = [list(map(int, input().split())) for _ in range(9)]

# 빈 칸 위치를 저장할 리스트
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

solve(0)
