import sys

input = sys.stdin.readline


def matrix_cal(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % 1000000007
    return C


def get_matrix(A, n):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 == 1:
            result = matrix_cal(result, A)
        A = matrix_cal(A, A)
        n //= 2
    return result


def solve(n):
    if n == 0:
        return 0
    A = [[1, 1], [1, 0]]
    ans = get_matrix(A, n)
    return ans[0][1]


num = int(input())
print(solve(num))