import sys
from collections import deque

input = sys.stdin.readline


def solve():
    if orders[0] != 1:
        return 0

    visited = [False] * (n+1)
    visited[1] = True
    q = deque([1])
    idx = 1

    while q:
        cur = q.popleft()
        children = []

        for neighbor in graph[cur]:
            if not visited[neighbor]:
                children.append(neighbor)
                visited[neighbor] = True

        # 다음 idx부터 children 수 만큼의 노드가 실제 자식인지 확인
        next_nodes = orders[idx:idx+len(children)]
        if set(children) != set(next_nodes):
            return 0

        q.extend(next_nodes)
        idx += len(children)

    return 1


n = int(input())
graph =[[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

orders = list(map(int, input().split()))

print(solve())
