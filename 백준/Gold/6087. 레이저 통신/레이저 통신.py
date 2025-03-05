import sys
import heapq
input = sys.stdin.readline


def solve():
    start_r, start_c = c_pos[0]
    end_r, end_c = c_pos[1]

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    dist = [[[float('inf')] * 4 for _ in range(W)] for _ in range(H)]

    q = []

    for i in range(4):
        dist[start_r][start_c][i] = 0
        heapq.heappush(q, [0, start_r, start_c, i])

    while q:
        mirrors, row, col, dir = heapq.heappop(q)

        if dist[row][col][dir] < mirrors:
            continue

        if row == end_r and col == end_c:
            return mirrors

        for i in range(4):
            dr, dc = directions[i]
            nr, nc = row + dr, col + dc

            new_mirrors = mirrors
            if i != dir:
                new_mirrors += 1

            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != '*':
                if new_mirrors < dist[nr][nc][i]:
                    dist[nr][nc][i] = new_mirrors
                    heapq.heappush(q, [new_mirrors, nr, nc, i])

    return -1


W, H = map(int, input().split())
board = [list(input()) for _ in range(H)]

c_pos = []
for r in range(H):
    for c in range(W):
        if board[r][c] == 'C':
            c_pos.append([r, c])

print(solve())