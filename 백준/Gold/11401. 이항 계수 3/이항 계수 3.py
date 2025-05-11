import sys

input = sys.stdin.readline
"""
큰 범위 수에서 이향 계수를 효율적으로 계산해야함
-> 페르마의 소정리를 이용해 모듈로 곱셈 역원을 구하여 계산
"""


def factorials(n):
    # 팩토리얼과 그 역원 테이블 계산
    fct = [1] * (n + 1)
    inv_fct = [1] * (n + 1)

    for i in range(2, n + 1):
        fct[i] = fct[i - 1] * i % MOD

    # 모듈러 역원 구하기 (페르마의 소정리 사용)
    inv_fct[n] = pow(fct[n], MOD - 2, MOD)

    for i in range(n - 1, 0, -1):
        inv_fct[i] = inv_fct[i + 1] * (i + 1) % MOD

    return fct, inv_fct


def solve():
    if k < 0 or k > n:
        return 0
    # fct: 팩토리얼 테이블, inv_fct: 역팩토리얼 테이블
    fct, inv_fct = factorials(n)
    return fct[n] * inv_fct[k] % MOD * inv_fct[n - k] % MOD


n, k = map(int, input().split())
MOD = 1000000007

print(solve())
