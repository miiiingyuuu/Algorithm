import sys

input = sys.stdin.readline


def spread_dust(room, r, c):
    # 미세먼지 확산 보드
    tmp = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if room[i][j] == -1:
                tmp[i][j] = -1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for x in range(r):
        for y in range(c):
            if room[x][y] <= 0:
                continue

            amount = room[x][y] // 5
            spread_cnt = 0

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= R or ny < 0 or ny >= C or room[nx][ny] == -1:
                    continue

                tmp[nx][ny] += amount
                spread_cnt += 1

            tmp[x][y] += room[x][y] - (amount * spread_cnt)

    return tmp


def air_cleaner_on(room, r, c, air_cleaner):
    top, bottom = air_cleaner

    # 위쪽 공기청정기 반시계 방향 순환
    for i in range(top - 1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(c-1):
        room[0][i] = room[0][i+1]
    for i in range(top):
        room[i][c-1] = room[i+1][c-1]
    for i in range(c-1, 1, -1):
        room[top][i] = room[top][i-1]
    room[top][1] = 0

    # 아래쪽 공기청정기 시계 방향 순환
    for i in range(bottom + 1, r-1):
        room[i][0] = room[i+1][0]
    for i in range(c-1):
        room[r-1][i] = room[r-1][i+1]
    for i in range(r-1, bottom, -1):
        room[i][c-1] = room[i-1][c-1]
    for i in range(c-1, 1, -1):
        room[bottom][i] = room[bottom][i-1]
    room[bottom][1] = 0


def solve(r, c, t, room):
    air_cleaner = []
    for i in range(R):
        if room[i][0] == -1:
            air_cleaner.append(i)

    # T초 동안 시뮬레이션
    for _ in range(t):
        room = spread_dust(room, r, c)
        air_cleaner_on(room, r, c, air_cleaner)

    ans = 2
    for i in range(R):
        ans += sum(room[i])

    return ans


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

result = solve(R, C, T, room)
print(result)