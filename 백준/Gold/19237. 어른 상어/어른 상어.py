import sys

input = sys.stdin.readline

'''
1번 상어만 남기까지의 시간
'''


def smell_check():
    # 냄새 표시 및 업데이트
    for i in range(N):
        for j in range(N):
            num, t = smell_board[i][j]
            if t > 0:
                smell_board[i][j] = (num, t - 1)

    for num, (x, y, _) in sharks_info.items():
        smell_board[x][y] = (num, k)


def move_sharks():
    # 상어 이동
    new_sharks = dict()
    visited = dict()  # 만나는 상어 체크

    for num in sorted(sharks_info.keys()):
        x, y, d = sharks_info[num]
        moved = False

        # 채취 없는 빈칸으로 우선순위에 따라 이동하기
        for dir in sharks_d_priorities[num][d - 1]:
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < N:
                if smell_board[nx][ny][1] == 0:
                    moved = True
                    break

        # 빈 칸이 없다면 자기 냄새 있는 칸으로 가기
        if not moved:
            for dir in sharks_d_priorities[num][d - 1]:
                nx, ny = x + dx[dir], y + dy[dir]
                if 0 <= nx < N and 0 <= ny < N:
                    if smell_board[nx][ny][0] == num:
                        break

        # 이동 후 다른 상어와 만나는지 체크, 번호가 작은 상어가 살아 남음
        if (nx, ny) in visited:
            if visited[(nx, ny)] < num:
                continue

        visited[(nx, ny)] = num
        new_sharks[num] = [nx, ny, dir]

    return new_sharks


def solve():
    for time in range(1, 1001):
        smell_check()
        sharks_moved = move_sharks()

        # sharks_moved 정보로 갱신
        sharks_info.clear()
        sharks_info.update(sharks_moved)

        if len(sharks_info) == 1 and 1 in sharks_info:
            return time

    return -1


N, M, k = map(int, input().split()) # N: 격자 크기, M: 상어가 있는 칸 수, k: 채취가 없어지는데 걸리는 시간
sharks_board = [list(map(int, input().split())) for _ in range(N)]
sharks_d = list(map(int, input().split()))   # 1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽
sharks_d_priorities = [[] for _ in range(M+1)]   # k번째 상어의 방향 우선 순: 위, 아래, 왼쪽, 오른쪽
for i in range(1, M+1):
    for _ in range(4):
        sharks_d_priorities[i].append(list(map(int, input().split())))

smell_board = [[(0, 0) for _ in range(N)] for _ in range(N)]    # 채취 남길 배열: (num, remain k)

# 상어 정보: (sharks_num: i, j, d)
sharks_info = dict()
for i in range(N):
    for j in range(N):
        if sharks_board[i][j]:
            sharks_info[sharks_board[i][j]] = (i, j, sharks_d[sharks_board[i][j] - 1])

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

print(solve())
