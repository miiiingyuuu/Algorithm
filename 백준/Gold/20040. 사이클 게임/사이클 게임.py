import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]
for i in range(1, m+1):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        print(i)
        break

    union(parent, a, b)

else:
    print(0)