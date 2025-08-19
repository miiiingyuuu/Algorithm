import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve():
    visited = [[False] * w for _ in range(h)]
    # 처음에는 열지 못하는 문이라도 순회하다가 열쇠를 얻으면 해당 문을 열고 가는 경우가 생길 수도 있으므로 문 위치를 저장할 리스트
    doors = [[] for _ in range(26)]
    q = deque()

    q.append((0, 0))
    visited[0][0] = True
    cnt = 0

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if visited[nx][ny]:
                continue

            n_cell = ex_board[nx][ny]
            if n_cell == '*':
                continue

            visited[nx][ny] = True

            # 문서인 경우와 문, 열쇠인 경우를 나눠 순회하기
            if n_cell == '$':
                cnt += 1
                q.append((nx, ny))
            elif 'A' <= n_cell <= 'Z':
                if n_cell.lower() in keys:
                    q.append((nx, ny))
                else:
                    doors[ord(n_cell) - ord('A')].append((nx, ny))
            elif 'a' <= n_cell <= 'z':
                # 없었던 열쇠인 경우 이전에 내가 방문한 곳 중에 열쇠가 없어 못 열었던 문이 있는지 체크 후 해당 문의 위치를 큐에 넣기
                if n_cell not in keys:
                    keys.add(n_cell)

                    # 해당 열쇠로 열 수 있는 문들 전부 열기
                    for door_x, door_y in doors[ord(n_cell) - ord('a')]:
                        q.append((door_x, door_y))
                    doors[ord(n_cell) - ord('a')] = []
                q.append((nx, ny))
            else:
                q.append((nx, ny))

    return cnt


t = int(input())
for tc in range(t):
    h, w = map(int, input().split())
    board = [list(input().strip()) for _ in range(h)]   # .: 빈 공간, *: 벽, $: 문, 대문자: 문, 소문자: 열
    keys = set(input().strip())

    # 열쇠가 없을 경우 빈 set
    if '0' in keys:
        keys = set()

    # 상근이의 위치를 위해 외곽에 지나갈 수 있는 '.'을 세우기
    ex_board = [['.'] * (w+2)]
    for row in board:
        ex_board.append(['.'] + row + ['.'])
    ex_board.append(['.'] * (w+2))

    h += 2
    w += 2

    print(solve())
