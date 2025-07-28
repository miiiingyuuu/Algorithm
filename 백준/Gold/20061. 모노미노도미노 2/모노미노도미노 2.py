import sys

input = sys.stdin.readline

'''
t = 1: (x, y), 2: (x, y), (x, y+1), 3: (x, y), (x+1, y)
'''


# 점수 체크 및 보드 최신화
def check_score(board):
    global score

    new_board = []
    cnt = 0

    # 모든 행이 1이라면 점수를 얻고, 해당 행은 없어짐
    for row in board:
        if all(row):
            cnt += 1
        else:
            new_board.append(row)

    for _ in range(cnt):
        new_board = [[0] * 4] + new_board

    while len(new_board) < 6:
        new_board = [[0] * 4] + new_board

    for i in range(6):
        board[i] = new_board[i]

    score += cnt


# 0, 1번째 행에 블록이 있는지 없는지 확인 후 보드 최신화
def check_zero_one(board):
    light = 0
    for i in range(2):
        if any(board[i]):
            light += 1

    for _ in range(light):
        board.pop()
        board.insert(0, [0] * 4)


# 블록 놓기
def drop_block(board, blocks):
    while True:
        # 0행부터 시작해서 다음 행에 블록이 있거나 범위를 벗어날때까지 내려가다가, 조건에 걸리면 그 곳에 블록을 놓기(1 처리)
        for x, y in blocks:
            if x + 1 >= 6 or board[x + 1][y]:
                for bx, by in blocks:
                    board[bx][by] = 1
                return

        # 행 값에 + 1 (수직으로 내려감)
        for i in range(len(blocks)):
            blocks[i][0] += 1


def solve(type, r, c):
    # 초록 보드에 놓기
    if type == 1:
        drop_block(green_board, [[0, c]])
    elif type == 2:
        drop_block(green_board, [[0, c], [0, c + 1]])
    else:
        drop_block(green_board, [[0, c], [1, c]])

    # 파란 보드에 놓기 (회전해서 생각)
    if type == 1:
        drop_block(blue_board, [[0, 3 - r]])
    elif type == 2:
        drop_block(blue_board, [[0, 3 - r], [1, 3 - r]])
    else:
        drop_block(blue_board, [[0, 3 - r], [0, 3 - (r + 1)]])

    # 점수 계산
    check_score(green_board)
    check_score(blue_board)

    # 0, 1 행에 따른 처리
    check_zero_one(green_board)
    check_zero_one(blue_board)


blue_board = [[0] * 4 for _ in range(6)]
green_board = [[0] * 4 for _ in range(6)]

score = 0

n = int(input())
for _ in range(n):
    t, x, y = map(int, input().split())
    solve(t, x, y)

print(score)

total_blocks = sum(sum(row) for row in green_board) + sum(sum(row) for row in blue_board)
print(total_blocks)
