import sys

input = sys.stdin.readline


def solve(N, edges):
    dist = [0] * (N + 1)

    for i in range(N):
        for start, end, time in edges:
            if dist[start] + time < dist[end]:
                dist[end] = dist[start] + time
                if i == N-1:
                    return True

    return False


T = int(input())
for tc in range(T):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    print("YES" if solve(N, edges) else "NO")
