import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


h, w, x, y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(h+x)]
A = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        A[i][j] = B[i][j]

        if i >= x and j >= y:
            A[i][j] -= A[i-x][j-y]

for row in A:
    print(*row)