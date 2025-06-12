import sys
from collections import deque

input = sys.stdin.readline

'''
이분 그래프를 판별하는 방법은 정점을 두 색 중 하나로 칠하면서 인접한 정점은 다른 색이 되도록 하면서 판별
만약 인접한 정점이 같은 색으로 칠해져야 한다면 이분 그래프가 아님
'''


def solve(v, graph):
    visited = [0] * (v+1)   # 0: 방문x, 1: 색1, -1: 색2
    q = deque()

    for start in range(1, v+1):
        if visited[start] == 0:
            q.append(start)
            visited[start] = 1

            while q:
                node = q.popleft()
                for next_node in graph[node]:
                    if visited[next_node] == 0:
                        visited[next_node] = -visited[node]
                        q.append(next_node)
                    elif visited[next_node] == visited[node]:
                        return False

    return True


t = int(input())

for _ in range(t):
    v, e = map(int, input().split())    # v: 정점 e: 간선
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    if solve(v, graph):
        print("YES")
    else:
        print("NO")