import sys

input = sys.stdin.readline


def find_parent(parent, x):
    # 경로 압축 기법을 사용한 find 연산
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, rank, a, b):
    # 랭크를 고려한 union 연산
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a == b:
        return False

    # 랭크가 낮은 노드를 랭크가 높은 노드 밑에 둠
    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

    return True

# 크루스칼 알고리즘을 이용한 최소 스패닝 트리 구현
v, e = map(int, input().split())
graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()

parent = [i for i in range(v + 1)]
rank = [0] * (v + 1)

ans = 0

for i in graph:
    c, a, b = i

    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if union_parent(parent, rank, a, b):
        ans += c

print(ans)
