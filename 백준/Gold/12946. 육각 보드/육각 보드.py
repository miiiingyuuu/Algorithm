import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


'''
X의 위치를 저장하고, 모든 X가 칠해지는 순서에 따라 필요한 색의 수가 달라지므로 dfs로 계산해야함
해당 색을 칠했을때의 주변에 X가 있는 경우만 고려하면 된다. 색을 칠한 주변에 X가 없다면 다른 X에는 똑같은 색을 칠해도 된다는 뜻
1. 색칠을 해보면 가능한 최대의 색의 경우는 3가지
2. 기본이 1개의 색 -> 칠한 블록 근처에 X가 있다면 그 곳은 다른 색으로 칠해야함 음수로 표시 -> 주변을 둘러보니 음수가 같은 수가 있다 = 3번째 색이 필요
'''


def solve(x, y):
    global ans
    ans = max(ans, 1)

    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'X':
            # 첫 번째 색을 쓴 상태에서 주변에 X가 있다면, 해당 블록은 두 번째 색으로 칠해야하므로 (-)처리로 표시를 해둠
            if visited[nx][ny] == 0:
                visited[nx][ny] = -visited[x][y]
                # 그리고 해당 위치의 주변에 다른 색을 고려해야하는 경우가 있는지 체크
                solve(nx, ny)
                ans = max(ans, 2)
            else:
                # 주변의 2가지 색을 모두 칠했다면 3번째 색으로도 칠해야 함
                if visited[nx][ny] == visited[x][y]:
                    ans = max(ans, 3)
                    return


n = int(input())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 0]
dy = [0, 1, 1, 0, -1, -1]

visited = [[0] * n for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'X' and visited[i][j] == 0:
            visited[i][j] = 1
            solve(i, j)

print(ans)
