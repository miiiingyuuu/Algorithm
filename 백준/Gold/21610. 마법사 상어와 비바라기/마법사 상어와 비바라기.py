import sys

input = sys.stdin.readline


'''
1. 이동 명령: 방향 d로 s거리 만큼 이동: 이동 시에는 범위를 벗어나면 처음으로 돌아가는 형태
2. 각 구름이 있는 칸에 물의 양 +1
3. 구름 삭제 -> 구현 필요 없네
4. 2에서 물의 양이 증가한 칸에서 대각선으로 거리가 1인 칸에 물이 있는 바구니의 수 만큼 물의 양 증가
5. 저장된 물이 2 이상인 칸은 물의 양이 2 줄어들고 구름이 생김 -> 3에서 구름이 사라진 칸이 아니여야 함
'''

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

water_bug = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def solve(d, s):
    global clouds

    new_clouds = []
    # 구름 이동 시키기
    for x, y in clouds:
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        new_clouds.append((nx, ny))

    # 구름이 있는 곳의 물양 +1
    for x, y in new_clouds:
        board[x][y] += 1

    # 물복사 버그
    bug_tar = []
    for x, y in new_clouds:
        cnt = 0
        for dir_x, dir_y in water_bug:
            nx = x + dir_x
            ny = y + dir_y
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0:
                cnt += 1

        bug_tar.append((x, y, cnt))

    for x, y, cnt in bug_tar:
        board[x][y] += cnt

    # 새 구름 생성(이전에 구름이 있었던 위치는 생기지 않음)
    prev_clouds = set(new_clouds)
    clouds = []
    for x in range(N):
        for y in range(N):
            if (x, y) in prev_clouds:
                continue

            if board[x][y] >= 2:
                board[x][y] -= 2
                clouds.append((x, y))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]   # 초기 구름 위치

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    solve(d, s)

print(sum(map(sum, board)))
