import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def solve(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = [(0, start)]   # (거리, 노드)

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for nxt in graph[now]:
            if distance[nxt] > dist + 1:
                distance[nxt] = dist + 1
                heapq.heappush(q, (distance[nxt], nxt))

    return distance


n, m, k, x = map(int, input().split())  # n:도시 개수, m:도로 개수, k:거리 정보, x:출발 도시 번호
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = solve(x)

ans = [i for i in range(1, n+1) if result[i] == k]

if ans:
    for c in sorted(ans):
        print(c)
else:
    print(-1)
