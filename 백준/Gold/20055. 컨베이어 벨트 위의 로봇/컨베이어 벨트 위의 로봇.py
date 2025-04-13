import sys
from collections import deque
input = sys.stdin.readline


n, k = map(int, input().split())
durability = list(map(int, input().split()))

line = deque(durability)
robots = deque([False] * (2*n))

cnt = 0
while True:
    cnt += 1

    # 벨트가 한 칸 회전
    line.rotate(1)
    robots.rotate(1)

    # 내리는 위치에 온 로봇은 제거
    robots[n-1] = False

    # 로봇이 이동
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and line[i+1] > 0:
            robots[i] = False
            robots[i+1] = True

            line[i+1] -= 1

    robots[n-1] = False

    # 로봇 올리기
    if not robots[0] and line[0] > 0:
        robots[0] = True
        line[0] -= 1

    if line.count(0) >= k:
        break

print(cnt)