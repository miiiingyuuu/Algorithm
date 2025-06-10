import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

'''
해당 graph의 0번째부터 시작하면서 방문여부를 체크하며 다음 노드와 연결되어 있는지 확인
'''


def solve(now, depth):
    global found
    if depth == 5:
        found = True
        return

    visited[now] = True
    for next_node in graph[now]:
        if not visited[next_node]:
            solve(next_node, depth + 1)
            if found:
                return

    visited[now] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

found = False
visited = [False] * n

for i in range(n):
    solve(i, 1)
    if found:
        break

print(1 if found else 0)