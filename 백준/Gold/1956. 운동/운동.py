import sys

input = sys.stdin.readline


def solve():
    # k: 중간에 거치는 노드, i: 출발 노드, j: 도착 노드
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    ans = INF
    for i in range(1, v+1):
        if graph[i][i] < ans:
            ans = graph[i][i]

    if ans == INF:
        return -1
    else:
        return ans


v, e = map(int, input().split())
INF = float('inf')
graph = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

print(solve())