import sys

input = sys.stdin.readline


n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

ans = 0
for i in range(n):
    j = (i + 1) % n
    ans += points[i][0] * points[j][1]
    ans -= points[j][0] * points[i][1]

ans = abs(ans) / 2

print(f'{ans:.1f}')