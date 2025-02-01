import sys
import heapq
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# v: 정점의 개수, e: 간선의 개수 입력받기
v, e = map(int, input().split())
k = int(input())  # 시작 정점의 번호
inf = int(1e9)    # 무한대 값 설정 (10억)

# 각 정점에 연결된 간선 정보를 저장할 그래프 초기화
graph =[[] * (v+1) for _ in range(v+1)]
# 각 정점까지의 최단 거리를 저장할 리스트 초기화
distance = [inf] * (v+1)

# 간선 정보 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())  # a: 시작 정점, b: 도착 정점, c: 가중치
    graph[a].append((b, c))  # a에서 b로 가는 가중치 c인 간선 정보 저장

def dijkstra(start):
    q = []  # 우선순위 큐 초기화
    # 시작 정점으로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드를 거쳐서 다른 노드로 이동하는 거리

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # 최단 거리 갱신
                heapq.heappush(q, (cost, i[0]))  # 우선순위 큐에 삽입


dijkstra(k)  # k번 정점에서 시작하는 다익스트라 알고리즘 수행

# 각 정점으로 가기 위한 최단 거리 출력
for i in range(1, v+1):
    if distance[i] == inf:  # 도달할 수 없는 경우
        print("INF")
    else:  # 도달할 수 있는 경우 거리 출력
        print(distance[i])