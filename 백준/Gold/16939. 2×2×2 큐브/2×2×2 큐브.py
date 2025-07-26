import sys

input = sys.stdin.readline

'''
정확히 한 번 돌려서 2x2x2 루빅스 큐브를 풀 수 있는가? -> 모든 면이 같은 색인 경우
색상은 1~6으로 표, 각 번호씩 총 4번 나옴
한번의 움직임은 90도 밖에 돌지 않음 -> 한 면당 시계, 반시계로 움직이므로 총 12번의 움직임 안에 완성이 되는지 확인
'''


def get_rotations():
    # 윗면 시계 / 반시계 방향 회전 (1, 2, 3, 4)
    u_cw = {
        3: 1, 4: 3, 2: 4, 1: 2,
        17: 5, 18: 6, 5: 13, 6: 14, 13: 21, 14: 22, 21: 17, 22: 18
    }
    u_ccw = {v: k for k, v in u_cw.items()}

    # 앞면 시계 / 반시계 방향 회전 (21, 22, 23, 24)
    f_cw = {
        23: 21, 21: 22, 24: 23, 22: 24,
        18: 1, 20: 2, 13: 11, 15: 12, 2: 13, 1: 15, 12: 18, 11: 20
    }
    f_ccw = {v: k for k, v in f_cw.items()}

    # 우측면 시계 / 반시계 방향 회전 (17, 18, 19, 20)
    r_cw = {
        19: 17, 17: 18, 20: 19, 18: 20,
        6: 2, 8: 4, 10: 6, 12: 8, 23: 10, 21: 12, 4: 21, 2: 23
    }
    r_ccw = {v: k for k, v in r_cw.items()}

    # 왼쪽면 시계 / 반시계 방향 회전 (13, 14, 15, 16)
    l_cw = {
        15: 13, 13: 14, 16: 15, 14: 16,
        24: 1, 22: 3, 1: 5, 3: 7, 5: 9, 7: 11, 9: 24, 11: 22
    }
    l_ccw = {v: k for k, v in l_cw.items()}

    # 뒷면 시계 / 반시계 방향 회전 (5, 6, 7, 8)
    b_cw = {
        7: 5, 5: 6, 8: 7, 6: 8,
        16: 3, 14: 4, 19: 9, 17: 10, 9: 14, 10: 16, 3: 17, 4: 19
    }
    b_ccw = {v: k for k, v in b_cw.items()}

    # 아랫면 시계 / 반시계 방향 회전 (9, 10, 11, 12)
    d_cw = {
        11: 9, 9: 10, 12: 11, 10: 12,
        15: 7, 16: 8, 23: 15, 24: 16, 19: 23, 20: 24, 7: 19, 8: 20
    }
    d_ccw = {v: k for k, v in d_cw.items()}

    return [u_cw, u_ccw, f_cw, f_ccw, r_cw, r_ccw, l_cw, l_ccw, b_cw, b_ccw, d_cw, d_ccw]


def cube_check(curr_cube):
    for i in range(0, 24, 4):
        if not (curr_cube[i] == curr_cube[i + 1] == curr_cube[i + 2] == curr_cube[i + 3]):
            return False
    return True


def cube_rotation(curr_cube, rotation_map):
    new_cube = list(curr_cube)
    for original_pos, new_pos in rotation_map.items():
        new_cube[new_pos - 1] = curr_cube[original_pos - 1]

    return new_cube


cube = list(map(int, input().split()))

rotations = get_rotations()

for rotation in rotations:
    rotated_cube = cube_rotation(cube, rotation)
    if cube_check(rotated_cube):
        print(1)
        exit()

print(0)
