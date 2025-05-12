import sys

input = sys.stdin.readline

"""
Union-Find 구조로 친구 관계가 생길때 마다 두 사람을 하나의 네트워크로 합치고, 그 집합의 크기를 출력
"""


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def solve(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a
        network_size[root_a] += network_size[root_b]

    return network_size[root_a]


t = int(input())
for _ in range(t):
    f = int(input())
    parent = {}
    network_size = {}

    for _ in range(f):
        f1, f2 = input().strip().split()

        if f1 not in parent:
            parent[f1] = f1
            network_size[f1] = 1
        if f2 not in parent:
            parent[f2] = f2
            network_size[f2] = 1

        print(solve(f1, f2))