import sys
from collections import deque

input = sys.stdin.readline


def solve():
    distance = [-1] * (n+1)
    distance[x] = 0
    q = deque([x])

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if distance[nxt] == -1:
                distance[nxt] = distance[now] + 1
                q.append(nxt)

    return distance


n, m, k, x = map(int, input().split())  # n:도시 개수, m:도로 개수, k:거리 정보, x:출발 도시 번호
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

result = solve()

ans = [i for i in range(1, n+1) if result[i] == k]

if ans:
    for c in sorted(ans):
        print(c)
else:
    print(-1)
