import sys
import heapq

input = sys.stdin.readline  # 빠른 입력을 위한 설정
inf = int(1e9)  # 무한대 값 설정

# 정점(V)과 간선(E) 개수 입력
V, E = map(int, input().split())
# 각 정점에 연결된 간선 정보를 저장할 그래프 초기화
graph = [[] for _ in range(V + 1)]

# 간선 정보 입력
# 양방향 그래프이므로 양쪽 정점에 모두 추가
for _ in range(E):
    x, y, cost = map(int, input().split())  # 시작점, 도착점, 비용
    graph[x].append((y, cost))
    graph[y].append((x, cost))


def dijkstra(s):
    """
    다익스트라 알고리즘으로 시작점에서 모든 정점까지의 최단 거리를 계산
    s: 시작 정점
    return: 시작점에서 각 정점까지의 최단 거리 리스트
    """
    distance = [inf] * (V + 1)  # 최단 거리 테이블을 무한대로 초기화
    q = []  # 우선순위 큐 생성
    heapq.heappush(q, (0, s))  # 시작점의 거리는 0
    distance[s] = 0

    while q:
        # 현재 가장 가까운 정점 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 정점과 연결된 다른 정점들 확인
        for i in graph[now]:
            cost = dist + i[1]  # 현재까지의 거리 + 다음 정점까지의 거리

            # 더 짧은 경로를 발견한 경우 업데이트
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


# 반드시 거쳐야 하는 두 정점 입력
v1, v2 = map(int, input().split())

# 1번 정점, v1, v2에서 시작하는 최단 거리 계산
first_distance = dijkstra(1)  # 1번 정점에서 시작
v1_distance = dijkstra(v1)    # v1에서 시작
v2_distance = dijkstra(v2)    # v2에서 시작

# 경로1: 1 -> v1 -> v2 -> V
v1_path = first_distance[v1] + v1_distance[v2] + v2_distance[V]
# 경로2: 1 -> v2 -> v1 -> V
v2_path = first_distance[v2] + v2_distance[v1] + v1_distance[V]

# 두 경로 중 더 짧은 경로 선택
result = min(v1_path, v2_path)
# 경로가 존재하지 않는 경우 -1 출력
print(result if result < inf else -1)