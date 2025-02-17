import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


def solve(x, n, graph):
    distance = [INF] * (n+1)
    distance[x] = 0
    q = []
    heapq.heappush(q, (0, x))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return distance


N, M, X = map(int, input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph1[a].append((b, c))
    graph2[b].append((a, c))

go_party = solve(X, N, graph1)
back_home = solve(X, N, graph2)

ans = 0
for i in range(1, N+1):
    t = go_party[i] + back_home[i]
    ans = max(ans, t)

print(ans)