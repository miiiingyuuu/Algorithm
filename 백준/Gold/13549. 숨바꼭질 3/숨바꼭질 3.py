import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, end):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        if x == end:
            return t[x]

        if -1 < x*2 < max_num and visited[x*2] == 0:
            q.appendleft(x*2)
            t[x*2] = t[x]
            visited[x*2] = 1

        if -1 < x-1 < max_num and visited[x-1] == 0:
            q.append(x-1)
            t[x-1] = t[x]+1
            visited[x-1] = 1

        if -1 < x+1 < max_num and visited[x+1] == 0:
            q.append(x+1)
            t[x+1] = t[x]+1
            visited[x+1] = 1


N, K = map(int, input().split())
max_num = 10**5+1
t = [0] * max_num
visited = [0] * max_num

print(bfs(N, K))
