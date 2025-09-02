import sys

input = sys.stdin.readline

papers = [0, 5, 5, 5, 5, 5]    # 각 색종이는 5장씩 있음
board = [list(map(int, input().split())) for _ in range(10)]
ans = float('inf')


def attach(x, y, size, status):
    # 0: 붙임, 1: 스티커 없음
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = status


def possible(x, y, size):
    # (x, y)를 왼쪽 가장 위라고 가정하고 붙이기: 색종이가 범위 안에 있고, 그 사이에 0이 없는 경우에 가능
    if x + size > 10 or y + size > 10:
        return False

    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] == 0:
                return False

    return True


def solve(cnt):
    global ans

    if cnt >= ans:
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for size in range(5, 0, -1):    # 큰 색종이부터 붙여보기
                    if papers[size] != 0 and possible(i, j, size):
                        attach(i, j, size, 0)
                        papers[size] -= 1
                        solve(cnt + 1)
                        papers[size] += 1
                        attach(i, j, size, 1)
                # 모든 1에 스티커를 다 붙이고 난 뒤에 붙일 곳이 없다면 ans를 갱신하고 더 이상 변화하면 안되기 때문에 return으로 끝냄
                return

    ans = min(ans, cnt)


solve(0) # 사용한 색종이 개수

print(ans if ans != float('inf') else -1)
