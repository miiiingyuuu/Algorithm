import sys

input = sys.stdin.readline


'''
드래곤 커브의 규칙을 찾아보면 끝점을 기준으로
0세대: 우
1세대: 우, 상 (상은 우를 90도 회전)
2세대: 우, 상, 좌, 상 (좌는 상을 90도 회전, 상은 우를 90도 회전)
3세대: 우, 상, 좌, 상, 좌, 하, 좌, 상 (좌는 상을 90도 회전, 하는 좌를 90도 회전, 상은 우를 90도 회전)
...
즉 n세대는 n-1세대의 커브를 -1번째 인덱스부터 90도 회전하여 붙인 것
101 * 101 board에 False를 표시하고 g세대 만큼 이동하며 해당하는 board는 True, 이후 네 꼭짓점이 모두 드래곤 커브에 포함이 되면 cnt++
'''


def solve(x, y, d, g):
    board[y][x] = True
    # 방향 리스트
    directions = [d]

    # g세대 만큼 진행
    for _ in range(g):
        # 이전 세대의 -1번째 인덱스부터 90도 회전 후 붙이기
        for i in range(len(directions) - 1, -1, -1):
            directions.append((directions[i] + 1) % 4)

    for direction in directions:
        x += dx[direction]
        y += dy[direction]
        if 0 <= x <= 100 and 0 <= y <= 100:
            board[y][x] = True


n = int(input())
# 방향: 우, 상, 좌, 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())  # x, y: 시작 위치, d: 방향, g: 세대
    solve(x, y, d, g)

cnt = 0
# 네 꼭짓점이 모두 True인 경우에 cnt++
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            cnt += 1

print(cnt)