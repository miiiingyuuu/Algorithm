import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve():
    # 플레이어가 여러명일 수 있음 -> 큐를 여러개 사용
    q = [deque() for _ in range(p)]
    result = [0] * p

    # 각 플레이어에 맞는 성 찾아서 큐에 추가하고 초기 개수 세기
    for i in range(n):
        for j in range(m):
            if board[i][j] != '.' and board[i][j] != '#':
                num = int(board[i][j]) - 1
                q[num].append((i, j))
                result[num] += 1

    while True:
        # 확장이 가능한지 체크하는 boolean
        done = True
        # 플레이어 순서대로 성 확장하기
        for i in range(p):
            # 플레이어가 더 이상 확장할 성이 없으면 끝(done = True)
            if not q[i]:
                continue

            done = False
            limit = limits[i]

            # 현재 플레이어의 성을 확장시킬 큐
            tmp_q = deque()
            while q[i]:
                x, y = q[i].popleft()
                tmp_q.append((x, y, 0)) # 좌표, 이동거리

            nq = deque()
            while tmp_q:
                x, y, dist = tmp_q.popleft()
                # 이동거리를 다 쓰면 현재턴에는 움직일 수 없음
                if dist == limit:
                    nq.append((x, y))
                    continue

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                        board[nx][ny] = str(i+1)
                        result[i] += 1
                        tmp_q.append((nx, ny, dist+1))

            # 다음 턴 시작 지점 갱신
            q[i] = nq

        if done:
            break

    return result


n, m, p = map(int, input().split())
limits = list(map(int, input().split()))
board = [list(input().strip()) for _ in range(n)]

print(*solve())
