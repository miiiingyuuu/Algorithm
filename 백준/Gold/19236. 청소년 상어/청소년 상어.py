import sys
import copy

input = sys.stdin.readline

'''
상어는 지나가는 방향으로만 갈 수 있음 방향 회전 x
상어가 행동한 후 -> 물고기 움직이기
'''


def solve(board, fish_info, shark_r, shark_c, cur_shark_d, cur_shark_size):
    global max_val

    # deepcopy
    board = copy.deepcopy(board)
    fish_info = copy.deepcopy(fish_info)

    # 물고기 이동
    for cur_fish in range(1, 17):
        if cur_fish not in fish_info:
            continue

        r, c, d = fish_info[cur_fish]
        for i in range(8):
            nd = (d + i) % 8
            nr, nc = r + directions[nd][0], c + directions[nd][1]
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark_r, shark_c):
                if board[nr][nc] != 0:
                    tar_fish = board[nr][nc]
                    fish_info[tar_fish][:2] = [r, c]  # tar_fish 좌표 변경(tar_fish는 방향은 안바뀜)
                board[r][c], board[nr][nc] = board[nr][nc], board[r][c]  # 번호 변경
                fish_info[cur_fish] = [nr, nc, nd]  # cur_fish 좌표 및 방향 변경
                break

    # 상어 이동
    for nxt in range(1, 4):
        # 해당 경로에 있는 물고기를 하나씩 먹는 경우를 구해야함 (1~4)
        shark_nr = shark_r + directions[cur_shark_d][0] * nxt
        shark_nc = shark_c + directions[cur_shark_d][1] * nxt
        if 0 <= shark_nr < 4 and 0 <= shark_nc < 4 and board[shark_nr][shark_nc] != 0:
            nxt_fish = board[shark_nr][shark_nc]
            shark_nd = fish_info[nxt_fish][2]

            # 상태 변경
            new_board = copy.deepcopy(board)
            new_fish_info = copy.deepcopy(fish_info)

            new_board[shark_r][shark_c] = 0
            new_board[shark_nr][shark_nc] = 0
            del new_fish_info[nxt_fish]

            solve(new_board, new_fish_info, shark_nr, shark_nc, shark_nd, cur_shark_size + nxt_fish)

        else:
            max_val = max(max_val, cur_shark_size)


arr = [[0] * 4 for _ in range(4)]
fish_data = dict()
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish_num = data[j * 2]
        fish_d = data[(j * 2) + 1] - 1  # 인덱스 번호 맞춰주기
        arr[i][j] = fish_num
        fish_data[fish_num] = [i, j, fish_d]

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# (0, 0) 물고기 먹음 처리
shark_size = arr[0][0]
shark_d = fish_data[shark_size][2]

arr[0][0] = 0
del fish_data[shark_size]

max_val = 0

solve(arr, fish_data, 0, 0, shark_d, shark_size)  # 상어의 위치, 상어의 방향, 상어의 크기

print(max_val)
