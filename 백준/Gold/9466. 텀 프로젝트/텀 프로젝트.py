import sys

input = sys.stdin.readline


T = int(input())
for t in range(T):
    n = int(input())
    chosen = [0] + list(map(int, input().split()))

    visited = [False] * (n+1)
    in_team = [False] * (n+1)

    for i in range(1, n+1):
        if visited[i]:
            continue

        now = i
        path = []

        while not visited[now]:
            visited[now] = True
            path.append(now)
            now = chosen[now]

        if now in path:
            cycle_start = path.index(now)
            for j in range(cycle_start, len(path)):
                in_team[path[j]] = True

    ans = sum(1 for i in range(1, n+1) if not in_team[i])
    print(ans)