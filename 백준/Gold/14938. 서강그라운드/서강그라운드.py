import sys

input = sys.stdin.readline


def dijkstra(start, n, m, items, graph):
    # 최단 거리 배열 초기화
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    # 방문 체크 배열
    visited = [False] * (n + 1)

    # 시작점에서의 아이템 수 계산 초기화
    items_sum = 0

    while True:
        # 최소 거리 찾기
        min_dist = float('inf')
        curr = -1

        # 방문하지 않은 노드 중 최단거리인 노드 찾기
        for i in range(1, n + 1):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                curr = i

        # 더 이상 방문할 노드가 없으면 종료
        if curr == -1:
            break

        visited[curr] = True

        # 현재 노드가 수색범위 내에 있다면 아이템 추가
        if distance[curr] <= m:
            items_sum += items[curr]

        # 인접한 노드들의 거리 갱신
        for next_node, weight in graph[curr]:
            if not visited[next_node]:
                distance[next_node] = min(distance[next_node], distance[curr] + weight)

    return items_sum


# 입력 받기
n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))  # 1-based indexing을 위해 [0] 추가

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 도로 정보 입력
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# 각 지점에서 시작했을 때의 최대 아이템 수 계산
max_items = 0
for start in range(1, n + 1):
    max_items = max(max_items, dijkstra(start, n, m, items, graph))

print(max_items)