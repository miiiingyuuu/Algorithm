import sys

input = sys.stdin.readline


N = int(input())
arr = [[-1] * 1001 for _ in range(1001)]

max_h, max_w = 0, 0
for i in range(N):
    r, c, w, h = map(int, input().split())

    if max_h < c + h:
        max_h = c + h

    for j in range(c, c + h):
        arr[j][r:(r + w)] = [i] * w

for n in range(N):
    cnt = 0
    for i in range(max_h):
        cnt += arr[i].count(n)

    print(cnt)