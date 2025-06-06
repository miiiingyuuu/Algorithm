import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

'''
처음부터 시작해서 해당 부분을 방문하지 않았고, 주변에 방문한 곳이 없다면 합에 쓸 수 있는 곳
그런식으로 max_val을 구하며 백트래킹 형식으로 ans를 구함
'''


def is_valid(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny]:
                return False

    return True


def solve(cnt, val, s):
    global ans
    if cnt == k:
        ans = max(ans, val)
        return

    for i in range(s, n*m):
        x = i // m
        y = i % m

        if not visited[x][y] and is_valid(x, y):
            visited[x][y] = True
            solve(cnt + 1, val + board[x][y], s + 1)
            visited[x][y] = False


n, m, k = map(int, input().split()) # k개를 선택
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = -1e9

solve(0, 0, 0)

print(ans)