import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(start, now):
    visited[start] = True  # 방문 체크 추가
    for next_node, weight in graph[start]:
        if not visited[next_node]:  # 방문하지 않은 노드만 탐색
            distance[next_node] = now + weight
            dfs(next_node, now + weight)

N = int(input())
graph = [[] for _ in range(N+1)]

# N-1개의 간선 정보를 입력받음
for _ in range(N-1):  
    p, c, d = map(int, input().split())
    graph[p].append((c, d))
    graph[c].append((p, d))

# 첫 번째 DFS - 임의의 노드(1)에서 가장 먼 노드 찾기
distance = [-1] * (N+1)
visited = [False] * (N+1)  # 방문 체크 배열 추가
distance[1] = 0
dfs(1, 0)

# 두 번째 DFS - 찾은 노드에서 가장 먼 노드까지의 거리 찾기
start = distance.index(max(distance))
distance = [-1] * (N+1)
visited = [False] * (N+1)  # 방문 체크 배열 초기화
distance[start] = 0
dfs(start, 0)

print(max(distance))