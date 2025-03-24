import sys

input = sys.stdin.readline


x, y, w, s = map(int, input().split())

tmp1 = (x * w) + (y * w)

if (x + y) % 2 == 0:
    tmp2 = max(x, y) * s
else:
    tmp2 = (max(x, y) - 1) * s + w

tmp3 = (min(x, y) * s) + (abs(x-y) * w)

print(min(tmp1, tmp2, tmp3))