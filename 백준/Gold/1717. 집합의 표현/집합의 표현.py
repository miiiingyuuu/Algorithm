import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]


def union_sets(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    order, num1, num2 = map(int, input().split())

    if order == 0:
        union_sets(num1, num2)
    else:
        if find_parent(num1) == find_parent(num2):
            print('YES')
        else:
            print('NO')