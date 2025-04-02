import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solve():
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n+1)]
    mst_edges = []

    for a, b, c in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst_edges.append(c)

    return sum(mst_edges) - max(mst_edges)


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

print(solve())