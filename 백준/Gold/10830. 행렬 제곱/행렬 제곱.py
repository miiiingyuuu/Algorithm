import sys

input = sys.stdin.readline


def matrix_multiply(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result


def matrix_power(A, B, N):
    if B == 1:
        return [[x % 1000 for x in row] for row in A]

    # B가 짝수인 경우
    if B % 2 == 0:
        temp = matrix_power(A, B // 2, N)
        return matrix_multiply(temp, temp, N)

    # B가 홀수인 경우
    else:
        temp = matrix_power(A, B - 1, N)
        return matrix_multiply(temp, A, N)


# 입력 받기
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산
result = matrix_power(A, B, N)

# 결과 출력
for row in result:
    print(*row)