import sys

input = sys.stdin.readline

'''
낚시왕은 C열 끝까지 이동하면 끝
다음 1초 간 일어나는 일
1. 낚시왕이 오른쪽으로 한 칸 이동 -> C+1까지 반복문 돌리기
2. 낚시왕이 열에 있는 상어 중 제일 가까운 상어를 잡음 -> 잡으면 상어는 사라짐
3. 이후에 상어가 해당 방향으로 속력만큼 칸을 이동 (벽에 부딪히면 반대 방향으로 남은 칸 수를 이동) -> 최적화를 위해 계산식을 구하기
4. 상어가 이동 한 후에 한 칸에 두 마리 이상의 상어가 있다면 크기가 큰 상어가 해당 칸의 상어를 모두 잡아 먹음 -> 크기를 비교하여 크다면 값 갱신
꼭 그래프를 그려 기록을 하기보다는 딕셔너리 형태로 키 벨류를 활용하여 푸는 방법도 꽤나 효율적인 것 같다
'''


def solve(sharks):
    caught_sharks_weight = 0

    # 낚시왕이 1번 열부터 C번 열까지 이동
    for fish_king in range(1, C+1):
        shark_to_catch = None

        # 해당 열에서 가장 가까운 상어 잡기
        for row in range(1, R+1):
            if (row, fish_king) in sharks:
                shark_to_catch = (row, fish_king)
                break

        # 상어를 잡았다면 크기를 더하고 상어 제거
        if shark_to_catch:
            speed, direction, size = sharks[shark_to_catch]
            caught_sharks_weight += size
            del sharks[shark_to_catch]

        # 상어 이동
        sharks_moved = {}
        for (r, c), (s, d, z) in sharks.items():
            nr, nc, nd = r, c, d

            if d <= 2:  # 상하 이동
                cycle = (R - 1) * 2
                s_mod = s % cycle

                if d == 1:  # 위
                    pos = r - s_mod
                else:  # 아래
                    pos = r + s_mod

                # 벽에 부딪히는 경우 위치와 방향 보정
                while pos < 1 or pos > R:
                    if pos < 1:
                        pos = 2 - pos
                        nd = 2
                    elif pos > R:
                        pos = 2 * R - pos
                        nd = 1
                nr = pos

            else:  # 좌우 이동
                cycle = (C - 1) * 2
                s_mod = s % cycle

                if d == 4:  # 왼쪽
                    pos = c - s_mod
                else:  # 오른쪽
                    pos = c + s_mod

                # 벽에 부딪히는 경우 위치와 방향 보정
                while pos < 1 or pos > C:
                    if pos < 1:
                        pos = 2 - pos
                        nd = 3
                    elif pos > C:
                        pos = 2 * C - pos
                        nd = 4
                nc = pos

            # 이동한 위치에 상어가 없거나, 있더라도 지금 상어가 더 크다면 업데이트
            if (nr, nc) not in sharks_moved or z > sharks_moved[(nr, nc)][2]:
                sharks_moved[(nr, nc)] = (s, nd, z)

        sharks = sharks_moved

    return caught_sharks_weight


R, C, M = map(int, input().split())
if M == 0:
    print(0)
    exit()

sharks = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r, c)] = (s, d, z)  # s: 속력, d: 방향, z: 크기

print(solve(sharks))
