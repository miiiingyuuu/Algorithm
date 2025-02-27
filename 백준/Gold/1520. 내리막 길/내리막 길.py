import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def solve(i, j):
    global memo

    if i == M-1 and j == N-1:
        return 1

    if (i, j) in memo:
        return memo[(i, j)]

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    paths = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < M and 0 <= nj < N and board[ni][nj] < board[i][j]:
            paths += solve(ni, nj)

    memo[(i, j)] = paths
    return paths


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
memo = {}

print(solve(0, 0))