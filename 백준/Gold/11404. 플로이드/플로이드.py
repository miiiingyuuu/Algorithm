import sys

input = sys.stdin.readline


N = int(input())
M = int(input())
INF = int(1e9)

graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for x in range(1, N+1):
    for y in range(1, N+1):
        if graph[x][y] == INF:
            print(0, end=' ')
        else:
            print(graph[x][y], end=' ')
    print()