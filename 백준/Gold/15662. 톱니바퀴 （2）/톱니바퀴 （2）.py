import sys
from collections import deque

input = sys.stdin.readline

'''
1번째 회전 시: 1톱니의 2_idx와 2톱니의 6_idx, 2톱니의 2_idx와 3톱니의 6_idx, 3톱니의 2_idx와 4톱니의 6_idx...
해당 톱니의 6번째와 왼쪽의 2번째, 2번째와 오른쪽의 6번째를 비교해서 움직일지 말지 체크하는 visited 배열을 만들어서 기록 후
deque의 rotate를 이용해서 반시계, 시계 방향으로 1칸 씩 이동
'''


def solve(tar, d, cogwheels):
    visited = [0] * t   # 회전 여부 확인용 visited - -1: 반시계, 0: 가만히, 1: 시계
    visited[tar] = d

    # tar 톱니에서 왼쪽 확인
    for i in range(tar, 0, -1):
        if cogwheels[i][6] != cogwheels[i-1][2]:
            visited[i-1] = -visited[i]
        else:
            continue

    # tar 톱니에서 오른쪽 확인
    for i in range(tar, t-1):
        if cogwheels[i][2] != cogwheels[i+1][6]:
            visited[i+1] = -visited[i]
        else:
            continue

    # 종합하여 회전
    for i in range(t):
        if visited[i] == 1:
            cogwheels[i].rotate(1)
        elif visited[i] == -1:
            cogwheels[i].rotate(-1)


t = int(input())

# 12시 방향부터 시계방향 순서의 톱니바퀴 정보
cogwheels = [deque(input().strip()) for _ in range(t)]  # 0: N극, 1: S극

k = int(input())    # 회전 횟수

for _ in range(k):
    tar, d = map(int, input().split())  # tar: 톱니번호, d: 돌릴 방향(-1: 반시계, 1: 시계)
    tar -= 1    # idx 번호 맞추기
    solve(tar, d, cogwheels)

# 12시가 S극(0)인 톱니 구하기
ans = 0
for i in range(t):
    if cogwheels[i][0] == '1':
        ans += 1

print(ans)
