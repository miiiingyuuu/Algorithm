import sys

input = sys.stdin.readline


N, M = map(int, input().split())
ban = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    ban[a][b] = True
    ban[b][a] = True

cnt = 0
for a in range(1, N-1):
    for b in range(a+1, N):
        if ban[a][b]:
            continue

        for c in range(b+1, N+1):
            if not ban[a][c] and not ban[b][c]:
                cnt += 1


print(cnt)
