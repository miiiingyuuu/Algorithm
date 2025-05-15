import sys
import heapq
input = sys.stdin.readline


def solve():
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            return cost

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                n_cost = cost + board[nx][ny]

                if n_cost < dist[nx][ny]:
                    dist[nx][ny] = n_cost
                    heapq.heappush(q, (n_cost, nx, ny))


num = 0
INF = float('inf')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    result = solve()
    num += 1

    print(f'Problem {num}: {result}')