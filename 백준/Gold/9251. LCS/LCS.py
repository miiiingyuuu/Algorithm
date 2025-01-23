import sys
input = sys.stdin.readline

tmp1 = list(input().strip())
tmp2 = list(input().strip())

N = len(tmp1)
M = len(tmp2)
lcs = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if tmp1[i-1] == tmp2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[N][M])