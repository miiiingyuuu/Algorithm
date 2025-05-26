import sys

input = sys.stdin.readline


def solve(line, l):
    visited = [False] * n

    for i in range(n-1):
        if line[i] == line[i+1]:    # 높이 차이가 없다면
            continue

        elif line[i] + 1 == line[i + 1]:    # 올라가는 경사로(우 -> 좌) 검사
            for j in range(i, i - l, -1):
                if j < 0 or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True

        elif line[i] - 1 == line[i + 1]:    # 내려가는 경사로(좌 -> 우) 검사
            for j in range(i+1, i+1+l):
                if j >= n or line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True
        else:
            return False

    return True


n, l = map(int, input().split())    # n: 크기, l: 경사로 길이
board = [list(map(int, input().split())) for _ in range(n)]

result = 0

# 행 검사
for row in board:
    if solve(row, l):
        result += 1

# 열 검사
for col in zip(*board):
    if solve(list(col), l):
        result += 1

print(result)