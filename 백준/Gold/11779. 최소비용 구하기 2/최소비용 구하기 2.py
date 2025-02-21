import sys
import heapq
input = sys.stdin.readline


def solve(start, end, info):
    graph = [[] for _ in range(N+1)]
    for s, e, c in info:
        graph[s].append((e, c))

    distances = [float('inf')] * (N+1)
    distances[start] = 0
    previous = [None] * (N+1)

    pq = [(0, start)]

    while pq:
        current_distance, current_location = heapq.heappop(pq)

        if current_distance > distances[current_location]:
            continue

        for next_location, cost in graph[current_location]:
            distance = current_distance + cost

            if distance < distances[next_location]:
                distances[next_location] = distance
                previous[next_location] = current_location
                heapq.heappush(pq, (distance, next_location))

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[end], len(path), path


N = int(input())
M = int(input())

info = []
for i in range(M):
    a, b, c = map(int, input().split())
    info.append((a, b, c))

start, end = map(int, input().split())

min_cost, path_length, path = solve(start, end, info)
print(min_cost)
print(path_length)
print(*path)