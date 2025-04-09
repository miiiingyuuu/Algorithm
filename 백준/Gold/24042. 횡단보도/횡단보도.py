import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def solve():
    INF = float('inf')
    # 시간 저장 리스트
    dist = [INF] * (n + 1)
    dist[1] = 0

    heap = [(0, 1)] # (time, node)

    while heap:
        time, node = heapq.heappop(heap)
        if dist[node] < time:
            continue

        for neighbor, offset in graph[node]:
            # 다음 파란불이 언제 들어오는지
            if time % m <= offset:
                next_time = time + (offset - (time % m))
            else:
                next_time = time + (m - (time % m) + offset)

            arrival = next_time + 1
            if dist[neighbor] > arrival:
                dist[neighbor] = arrival
                heapq.heappush(heap, (arrival, neighbor))

    return dist[n]


n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

print(solve())