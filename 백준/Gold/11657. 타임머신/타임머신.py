import sys

input = sys.stdin.readline


def solve(start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    for i in range(n-1):
        for a, b, c in bus_info:
            if dist[a] != float('inf') and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c

    negative_cycle = False
    cycle = [False] * (n + 1)

    for _ in range(n):
        for a, b, c in bus_info:
            if dist[a] != float('inf') and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c
                cycle[b] = True
                negative_cycle = True

    if negative_cycle:
        for _ in range(n):
            for a, b, c in bus_info:
                if cycle[a]:
                    cycle[b] = True

    return dist, cycle


n, m = map(int, input().split())
bus_info = [list(map(int, input().split())) for _ in range(m)]

distances, cycle = solve(1)

if any(cycle[2:n+1]):
    print(-1)
else:
    for i in range(2, n+1):
        if distances[i] == float('inf'):
            print(-1)
        else:
            print(distances[i])