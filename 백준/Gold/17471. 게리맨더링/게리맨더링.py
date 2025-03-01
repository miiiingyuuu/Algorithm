import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def is_connected(graph, areas):
    if not areas:
        return False

    start = list(areas)[0]
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor in areas and neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return len(visited) == len(areas)


N = int(input())
populations = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    for j in range(1, info[0]+1):
        graph[i].append(info[j])

ans = 1e99999
all_areas = set(range(1, N+1))

for k in range(1, N):
    for area1 in combinations(range(1, N+1), k):
        area1 = set(area1)
        area2 = all_areas - area1

        if is_connected(graph, area1) and is_connected(graph, area2):
            pop1 = sum(populations[a-1] for a in area1)
            pop2 = sum(populations[a-1] for a in area2)
            ans = min(ans, abs(pop1 - pop2))

if ans != 1e99999:
    print(ans)
else:
    print(-1)