import sys
from collections import deque

input = sys.stdin.readline


'''
매 초 1열씩 없어지는데, 이때 탈출이 가능한가? -> (N, j)에 도달하면 탈출 가능
왼쪽 <-> 오른쪽 점프를 할 때는 k칸 만큼 앞으로 이동하면서 점프
'''


def solve(r, c, t):
    visited = [[False] * N for _ in range(2)]
    visited[r][c] = True

    q = deque()
    q.append((r, c, t))

    while q:
        x, y, time = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 다리를 건너는 경우
            if 0 <= nx < 2 and 0 <= ny < N and lines[nx][ny] == '1' and ny > time and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, time + 1))

            # y 값이 N을 넘어 탈출이 가능한지 체크
            elif 0 <= nx < 2 and ny >= N:
                return 1

    return 0


N, k = map(int, input().split())
lines = [list(input().strip()) for _ in range(2)]

# 방향 위, 아래, 오른쪽, 왼쪽 -> 위, 아래 방향으로 갈때는 y가 k만큼 더 가야됨
dx = [-1, 1, 0, 0]
dy = [k, k, 1, -1]

print(solve(0, 0, 0)) # (r, c, t): t 이하의 발판으로는 점프 불가능
