import sys
import copy
input = sys.stdin.readline


def watch(room, x, y, d):
    for nd in d:
        nx, ny = x, y
        while True:
            nx += directions[nd][0]
            ny += directions[nd][1]
            if 0 <= nx < n and 0 <= ny < m:
                if room[nx][ny] == 6:
                    break
                if room[nx][ny] == 0:
                    room[nx][ny] = '#'
            else:
                break


def solve(depth, room):
    global ans

    # 설치된 cctv를 모두 돌고 0의 개수 세기
    if depth == len(cameras):
        count = sum(row.count(0) for row in room)
        ans = min(ans, count)
        return

    # cctv가 바라보는 방향으로 dfs를 돌며 사각지대의 최솟값 얻기
    num, x, y = cameras[depth]
    for d in cctv_directions[num]:
        tmp_room = copy.deepcopy(room)
        watch(tmp_room, x, y, d)
        solve(depth + 1, tmp_room)


n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

# cctv가 한번에 보는 방향
cctv_directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

# 카메라 찾기
cameras = []
for i in range(n):
    for j in range(m):
        if 1 <= room[i][j] <= 5:
            cameras.append((room[i][j], i, j))   # 카메라 번호, 카메라 좌표(x, y)

# 최솟값 구하기
ans = float('inf')

solve(0, room)

print(ans)