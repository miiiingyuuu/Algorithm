import sys
import math
input = sys.stdin.readline


r, c, w = map(int, input().split())

ans = 0
for i in range(w):  # w개의 줄
    row = r + i
    for j in range(i+1):    # c부터 c+i까지
        col = c + j
        ans += math.comb(row - 1, col - 1)

print(ans)