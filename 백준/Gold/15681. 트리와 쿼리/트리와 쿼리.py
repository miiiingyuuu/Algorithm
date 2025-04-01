import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solve(node, parent):
    subtree_size[node] = 1

    for i in graph[node]:
        if i != parent:
            solve(i, node)
            subtree_size[node] += subtree_size[i]


n, r, q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree_size = [0] * (n+1)

solve(r, -1)

for _ in range(q):
    queries = int(input())
    print(subtree_size[queries])