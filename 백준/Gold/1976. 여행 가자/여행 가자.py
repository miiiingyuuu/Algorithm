import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        parent[root_b] = root_a


n = int(input())
m = int(input())
parent = [i for i in range(n+1)]    # 초기에는 자기 자신이 부모

for i in range(1, n+1):
    info = list(map(int, input().split()))
    for j in range(1, n+1):
        if info[j-1] == 1:
            union(parent, i, j)

plan = list(map(int, input().split()))
root = find(parent, plan[0])

#  모든 도시가 같은 루트를 가지는지 확인
for city in plan:
    if find(parent, city) != root:
        print("NO")
        break

else:
    print("YES")