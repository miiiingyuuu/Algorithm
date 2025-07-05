import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline


'''
모든 SCV를 파괴하기 위한 최소 공격 횟수
한 번의 공격: 1st = 9, 2nd = 3, 3rd = 1 (0 <= SCV <= 3)
뮤탈이 공격할 수 있는 순열을 활용하여 visited[i][j][k](i, j, k = SCV 체력)에 방문여부를 확인하며 q에 cnt를 추가하여 답을 구하는 방식
'''


def solve():
    attack_cases = list(set(permutations([9, 3, 1])))

    # SCV가 3마리가 아닌 경우도 있으므로, 0을 임의로 추가해서 오류가 발생하지 않게 하기
    while len(SCV) < 3:
        SCV.append(0)

    # 각 SCV의 체력 방문 여부 확인, SCV의 최대 체력은 60
    visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]
    q = deque()

    a, b, c = SCV
    q.append((a, b, c, 0))  # a, b, c: 체력, 0: 공격 횟수
    visited[a][b][c] = True

    while q:
        x, y, z, cnt = q.popleft()

        if x <= 0 and y <= 0 and z <= 0:
            return cnt

        for dmg in attack_cases:
            nx = max(0, x - dmg[0])
            ny = max(0, y - dmg[1])
            nz = max(0, z - dmg[2])

            if not visited[nx][ny][nz]:
                visited[nx][ny][nz] = True
                q.append((nx, ny, nz, cnt + 1))


n = int(input())
SCV = list(map(int, input().split()))

print(solve())
