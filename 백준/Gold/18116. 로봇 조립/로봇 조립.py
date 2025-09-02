import sys

input = sys.stdin.readline


N = int(input())
MAX = 10**6 + 1
parent = [i for i in range(MAX)]
size = [1] * MAX    # 각 집합의 크기 저장


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return

    # 큰 집합 쪽에 작은 집합을 붙이기
    if size[a] < size[b]:
        a, b = b, a

    parent[b] = a
    size[a] += size[b]


for _ in range(N):
    order = input().split()
    if order[0] == 'I':
        a, b = int(order[1]), int(order[2])
        union(a, b)
    else:
        c = int(order[1])
        root = find(c)
        print(size[root])
