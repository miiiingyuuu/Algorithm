import sys
from collections import deque

input = sys.stdin.readline

'''
열어야 하는 문을 최소로
탈출을 하려면 외각에 있는 문이나 빈 칸으로 나가야 됨

'''


def solve(start_x, start_y, prison_map):
    # 문을 연 횟수를 저장할 visited
    visited = [[-1] * (m+2) for _ in range(n+2)]

    q = deque()
    q.append((start_x, start_y))

    # 처음 시작 위치를 0 처리: 문을 연 방향으로 갈 때마다 이전 칸 + 1
    visited[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n + 2 and 0 <= ny < m + 2:
                if prison_map[nx][ny] == '*' or visited[nx][ny] != -1:
                    continue

                if prison_map[nx][ny] == '#':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))

    return visited


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    board = [list(input().strip()) for _ in range(n)]  # *: 지나갈 수 없는 벽, .: 빈 공간, #: 문, $: 죄수의 위치

    # 상근이가 이동할 외각 이동 구간 만들기
    prison_board = [['.'] * (m + 2)]
    for row in board:
        prison_board.append(['.'] + row + ['.'])
    prison_board.append(['.'] * (m + 2))

    # 죄수의 위치 큐에 담기
    prisoners = []
    for i in range(n+2):
        for j in range(m+2):
            if prison_board[i][j] == '$':
                prisoners.append((i, j))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 한명씩 차례로 움직이게 해보기
    dist0 = solve(0, 0, prison_board)
    dist1 = solve(prisoners[0][0], prisoners[0][1], prison_board)
    dist2 = solve(prisoners[1][0], prisoners[1][1], prison_board)

    # 답 구하기
    ans = float('inf')
    for i in range(n + 2):
        for j in range(m + 2):
            if dist0[i][j] == -1 or dist1[i][j] == -1 or dist2[i][j] == -1:
                continue

            tmp = dist0[i][j] + dist1[i][j] + dist2[i][j]

            # 세 경로 모두 문을 지난 경우, 해당 문을 중복으로 열었으므로 -2 해줌
            if prison_board[i][j] == '#':
                tmp -= 2
            ans = min(ans, tmp)

    print(ans)
