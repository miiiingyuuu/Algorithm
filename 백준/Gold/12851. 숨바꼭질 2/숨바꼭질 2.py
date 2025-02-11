import sys
from collections import deque
input = sys.stdin.readline


def solve(N, K):
    MAX = 100001
    time = [-1] * MAX
    count = [0] * MAX

    q = deque()
    q.append(N)
    time[N] = 0
    count[N] = 1

    while q:
        x = q.popleft()

        for next_x in [x-1, x+1, x*2]:
            if 0 <= next_x < MAX:
                if time[next_x] == -1:
                    time[next_x] = time[x] + 1
                    count[next_x] = count[x]
                    q.append(next_x)

                elif time[next_x] == time[x] + 1:
                    count[next_x] += count[x]

    return time[K], count[K]


N, K = map(int, input().split())

min_time, ways = solve(N, K)
print(min_time)
print(ways)