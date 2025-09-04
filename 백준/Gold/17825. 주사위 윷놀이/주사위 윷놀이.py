import sys

input = sys.stdin.readline

'''
시작 칸에 4개의 말
10의 배수인 칸에 도착하면 다음 이동은 10->13, 20->22, 30->28로 가야함
말이 이동을 마치는 칸에 다른 말이 있다면, 그 말은 선택할 수 없음
1. 해당 말을 끝까지 보내고 주사위 횟수가 남았다면 추가적인 말 보내기
2. 말을 일단 다 꺼내기?
'''

# 주사위를 던졌을때 갈 수 있는 위치 정리 (1 ~ 5의 눈금)
board = [
    [1], [2], [3], [4], [5],
    [6, 21], [7], [8], [9], [10],
    [11, 25], [12], [13], [14], [15],
    [16, 27], [17], [18], [19], [20],
    [32], [22], [23], [24], [30],
    [26], [24], [28], [29], [24],
    [31], [20], [32]
]

points = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 13, 16, 19, 25,
    22, 24, 28, 27, 26,
    30, 35, 0
]


def move(now, dice):
    # 파란 칸 위인지 확인 후 가는 방향 정하기(이때 한칸을 이동함)
    if len(board[now]) == 2:
        now = board[now][1]
    else:
        now = board[now][0]

    # 주사위 눈금 만큼 움직이기(1칸 덜 움직이기: 위에서 움직였으므로)
    for _ in range(1, dice):
        now = board[now][0]

        if now == 32:
            break

    return now


def solve(turn, score, horses):
    global ans

    # 10번의 턴이 끝나면 max 값 찾기
    if turn == 10:
        ans = max(ans, score)
        return

    dice = dices[turn]

    # 4개의 말 중 하나 고르기
    for i in range(4):
        now = horses[i]
        # 도착한 말은 이동 불가
        if now == 32:
            continue

        nxt = move(now, dice)
        # 도착하려는 칸에 말이 이미 있으면 갈 수 없음
        if nxt != 32 and nxt in horses:
            continue

        horses[i] = nxt
        solve(turn + 1, score + points[nxt], horses)
        horses[i] = now # 백트래킹 후 원상복귀


dices = list(map(int, input().split()))

ans = 0

solve(0, 0, [0, 0, 0, 0])    # turn, score, horses

print(ans)
