import sys

input = sys.stdin.readline


def dfs(start, graph):
    visited = [-1] * (V + 1)
    visited[start] = 0
    stack = [(start, 0)]
    max_distance = 0
    max_node = start

    while stack:
        current, distance = stack.pop()

        if current in graph:  # 그래프에 해당 노드가 있는지 확인
            for next_node, weight in graph[current]:
                if visited[next_node] == -1:
                    next_distance = distance + weight
                    visited[next_node] = next_distance
                    stack.append((next_node, next_distance))

                    if next_distance > max_distance:
                        max_distance = next_distance
                        max_node = next_node

    return max_node, max_distance


# 입력 받기
V = int(input())
graph = {}  # 일반 딕셔너리 사용

# 그래프 구성
for i in range(V):
    line = list(map(int, input().split()))
    node = line[0]

    # 현재 노드의 간선 리스트 초기화
    if node not in graph:
        graph[node] = []

    j = 1
    while line[j] != -1:
        # 양방향 간선 추가
        next_node = line[j]
        weight = line[j + 1]

        # 현재 노드에서 다음 노드로 가는 간선 추가
        graph[node].append((next_node, weight))

        # 다음 노드에서 현재 노드로 가는 간선 추가
        if next_node not in graph:
            graph[next_node] = []
        graph[next_node].append((node, weight))

        j += 2

# 1. 임의의 정점(여기서는 1)에서 가장 먼 정점 찾기
farthest_node, _ = dfs(1, graph)

# 2. 찾은 정점에서 가장 먼 정점까지의 거리 구하기
_, diameter = dfs(farthest_node, graph)

print(diameter)