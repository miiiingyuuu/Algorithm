import sys
from collections import deque

input = sys.stdin.readline
'''
1 is S: +1, 2 is S: +2, 3 is S: +4, 4 is S: +8
1: 2번째, 2: 2, 6 번째, 3: 2, 6 번째, 4: 6번째
극이 같다면 회전 x, 극이 다르다면 반대로 회전
'''


def solve(idx, d):
    # 회전 여부 확인용 visited -> -1: 시계 반대 방향, 0: 가만히, 1: 시계 방향
    visited = [0] * 4
    visited[idx] = d

    # 왼쪽 확인
    for i in range(idx, 0, -1):
        if cogwheels[i][6] != cogwheels[i - 1][2]:
            visited[i - 1] = -visited[i]
        else:
            break

    # 오른쪽 확인
    for i in range(idx, 3):
        if cogwheels[i][2] != cogwheels[i + 1][6]:
            visited[i + 1] = -visited[i]
        else:
            break

    # 종합하여 회전하기
    for i in range(4):
        if visited[i] == 1:
            cogwheels[i].rotate(1)
        elif visited[i] == -1:
            cogwheels[i].rotate(-1)


cogwheels = [deque(input().strip()) for _ in range(4)]  # 4개의 톱니바퀴, 12시부터 시계방향 순서, 0: n극, 1: s극
k = int(input())  # 회전 횟수
for _ in range(k):
    idx, d = map(int, input().split())  # idx: 회전시킬 톱니바퀴 번호, d: 방향(1: 시계, -1: 반시계)
    idx -= 1

    solve(idx, d)

# 답 구하기
ans = 0
for i in range(4):
    if cogwheels[i][0] == '1':
        ans += (2 ** i)

print(ans)
