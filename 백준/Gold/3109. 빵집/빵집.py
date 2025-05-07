import sys

input = sys.stdin.readline


def solve(x, y):
    # 마지막 열에 도착하면 끝
    if y == c-1:
        return True

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if solve(nx, ny):
                    return True

    return False


r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

# 파이프를 겹쳐 놓을 수 없으니 방문 표시
visited = [[False] * c for _ in range(r)]

# 오른쪽 위, 오른쪽, 오른쪽 아래
directions = [(-1, 1), (0, 1), (1, 1)]

ans = 0
# 0번쨰 열에서 시작해서 r번째 행까지 파이프를 놓을 수 있는지 체크
for i in range(r):
    if board[i][0] == '.':
        if solve(i, 0):
            ans += 1

print(ans)