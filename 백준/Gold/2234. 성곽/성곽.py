import sys
from collections import deque

input = sys.stdin.readline

'''
1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
벽의 상태는 서쪽 벽: 1, 북쪽 벽: 2, 동쪽 벽: 4, 남쪽 벽: 8의 합한 값으로 나옴
-> 4방향의 벽에 대해 방문하려는 방향대로 8, 4, 2, 1을 빼주면 해당 방향에는 벽이 있어서 갈 수 없음 (이진수 합의 특성)
'''


def solve(x, y, rooms):
    global rooms_dimensions
    # 이 방의 넓이
    dimension = 1

    visited[x][y] = rooms
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()
        walls = board[r][c]

        for d in range(4):
            # 8, 4, 2, 1 순으로 순회하면서 해당 숫자보다 크다면 해당 방향으로 벽이 있다는 뜻이므로 빼고 다음으로 넘어 감
            if walls >= walls_d[d]:
                walls -= walls_d[d]
            else:
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == -1:
                    dimension += 1
                    visited[nr][nc] = rooms
                    q.append((nr, nc))

    # 해당 방의 넓이를 추가하기
    rooms_dimensions.append(dimension)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

# 추후에 인접한 방인지 비교하기 위해 -1로 방의 숫자를 초기화 해줌
visited = [[-1] * n for _ in range(m)]

# 해당 방향에 벽이 있음을 표시
walls_d = [8, 4, 2, 1]

# 벽의 방향에 맞게 보는 방향 설정
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

rooms = 0
rooms_dimensions = []
# board를 순회하면서 visited가 표시되지 않은 곳에서 출발해서 방의 개수 및 가장 넓은 방의 넓이 세기
for i in range(m):
    for j in range(n):
        if visited[i][j] == -1:
            rooms += 1
            solve(i, j, rooms)

# 하나의 벽을 제거하여 얻을 수 있는 가장 큰 넓이
# visited 배열을 각 방의 번호로 잡고, 인접한 배열의 번호가 다르다면 해당 벽을 허물어 넓이의 합을 구함
biggest = 0
for i in range(m):
    for j in range(n):
        for k in range(4):
            ni = i + dr[k]
            nj = j + dc[k]
            if -1 < ni < m and -1 < nj < n and visited[i][j] != visited[ni][nj]:
                biggest = max(biggest, rooms_dimensions[visited[i][j] - 1] + rooms_dimensions[visited[ni][nj] - 1])

print(rooms)
print(max(rooms_dimensions))
print(biggest)
