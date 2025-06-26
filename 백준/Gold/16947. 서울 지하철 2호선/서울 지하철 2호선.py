import sys
from collections import deque

sys.setrecursionlimit(10000)
input = sys.stdin.readline


'''
dfs로 사이클을 찾고, 사이클에 포함된 노드를 기록
bfs로 각 노드의 최단 거리 계산
'''


def solve(prev, cur, path):
    # 사이클 찾기 (dfs)
    global found
    if found:
        return

    visited[cur] = True
    path.append(cur)

    for neighbor in graph[cur]:
        if not visited[neighbor]:
            solve(cur, neighbor, path)
        # 방문한 적 있는 노드를 다시 만났는데, 그것이 부모가 아니고 아직 사이클을 발견한 상태가 아니라면 사이클이 발생
        elif neighbor != prev and not found:
            # 사이클 발견
            cycle_start = path.index(neighbor)
            for i in range(cycle_start, len(path)):
                cycle[path[i]] = True
            found = True
            return

    if not found:
        path.pop()


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
# 사이클이 발생하는 곳을 나타내기 위한 cycle
cycle = [False] * (n+1)
found = False

solve(0, 1, [])

# 거리 계산 bfs
dist = [-1] * (n+1)
q = deque()

for i in range(1, n+1):
    if cycle[i]:
        dist[i] = 0
        q.append(i)

while q:
    now = q.popleft()
    for neighbor in graph[now]:
        if dist[neighbor] == -1:
            dist[neighbor] = dist[now] + 1
            q.append(neighbor)

print(' '.join(map(str, dist[1:])))
