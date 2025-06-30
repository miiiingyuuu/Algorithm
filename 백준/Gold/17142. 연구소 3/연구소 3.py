import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

'''
연구소2와 다르게 활성화 되지 않은 바이러스가 있는 위치까지는 바이러스가 퍼질 필요가 없어서 시간이 다르게 나옴
연구소2는 1이 아닌 곳을 다 가게했다면, 얘는 0인 곳만 가면 되는 것 같음
+ 조건이 비활성 바이러스가 비활성 바이러스를 만나면 발동이 되버리네... 조건을 좀 더 추가할 필요가 있음
'''


def solve(comb):
    # 방문 표시할 겸 시간을 체크할 2차원 배열
    visited = [[-1] * n for _ in range(n)]
    q = deque()

    for x, y in comb:
        visited[x][y] = 0
        q.append((x, y))

    time = 0
    spread = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                # 방문하지 않았고, 벽이 아니라면 시간을 증가시키기
                if board[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # 벽으로 퍼졌을 경우에만 시간 체크 및 spread + 1 하기, 2로 갔을때는 바이러스를 활성화한 경우(방에 바이러스가 퍼진게 아님)
                    if board[nx][ny] == 0:
                        spread += 1
                        time = max(time, visited[nx][ny])

    return time if spread == empty_cnt else -1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 바이러스의 위치와 모든 방에 바이러스가 퍼졌는지 확인할 virus_loc 리스트와 empty_cnt 변수
virus_loc = []
empty_cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_loc.append((i, j))
        elif board[i][j] == 0:
            empty_cnt += 1

# 어떠한 경우에도 방에 다 퍼지지 않았다면 val 값은 모두 -1가 됨 -> ans가 1e9999로 변동이 없다면 모든 방에 퍼지는 경우가 없는 것
ans = 1e9999
for comb in combinations(virus_loc, m):
    val = solve(comb)
    if val != -1:
        ans = min(ans, val)

print(ans if ans != 1e9999 else -1)
