import sys

input = sys.stdin.readline


'''
1정육면체: 6, 2정육면체: 10, 3정육면체: 14, 4정육면체: 18 n개의 정육면체의 겉넓이: (n*4) + 2
'''


def solve():
    ans = 0

    for i in range(n):
        for j in range(m):
            tmp_val = board[i][j] * 4 + 2

            for d in range(4):
                ni = i + directions[d][0]
                nj = j + directions[d][1]
                if 0 <= ni < n and 0 <= nj < m:
                    min_val = min(board[i][j], board[ni][nj])
                    tmp_val -= min_val

            ans += tmp_val

    return ans


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(solve())
