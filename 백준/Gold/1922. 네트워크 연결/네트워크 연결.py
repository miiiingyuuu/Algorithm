import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solve():
    total_cost = 0
    for cost, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost

    return total_cost


N = int(input())
M = int(input())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(N+1)]

print(solve())
