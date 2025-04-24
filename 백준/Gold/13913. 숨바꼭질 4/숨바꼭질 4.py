import sys
from collections import deque
input = sys.stdin.readline


def solve(n, k):
    visited = [-1] * 100001 # 시간 기록
    path = [-1] * 100001    # 경로 기록

    q = deque()
    q.append(n)
    visited[n] = 0

    while q:
        cur = q.popleft()

        if cur == k:
            break

        for next_pos in (cur - 1, cur + 1, cur * 2):
            if 0 <= next_pos < 100001 and visited[next_pos] == -1:
                visited[next_pos] = visited[cur] + 1
                path[next_pos] = cur
                q.append(next_pos)

    route = []
    pos = k
    while pos != -1:
        route.append(pos)
        pos = path[pos]
    route.reverse()

    print(visited[k])
    print(*route)


n, k = map(int, input().split())
solve(n, k)