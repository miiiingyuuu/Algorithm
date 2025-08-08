import sys

input = sys.stdin.readline


'''
2x2 정사각형으로 나누고, 두 번째로 큰 숫자만 계속 남겼을 때, 마지막으로 남는 숫자는?
N을 2로 계속 나눠서 2가 될때 2x2에서 2번째로 큰 값을 찾는 식으로 재귀를 돌리면 될 듯?
'''


def solve(x, y, size):
    if size == 2:
        nums = [
            board[x][y], board[x][y+1], board[x+1][y], board[x+1][y+1]
        ]
        nums.sort(reverse=True)

        return nums[1]  # 두 번째로 큰 값

    half = size // 2

    vals = [
        solve(x, y, half),
        solve(x+half, y, half),
        solve(x, y+half, half),
        solve(x+half, y+half, half)
    ]
    vals.sort(reverse=True)

    return vals[1]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(solve(0, 0, N))
