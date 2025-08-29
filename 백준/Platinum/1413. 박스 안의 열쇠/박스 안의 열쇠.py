import sys
import math

input = sys.stdin.readline


'''
모든 열쇠와 상자의 경우의 수는 N!이 됨
M개의 폭탄으로 열 수 있는 상자의 최대치는 M개의 사이클
-> 순열의 사이클 개수 <= M이면 모두 열 수 있고, 사이클 개수 > M이면 전부 열지 못함
'''


def solve():
    # c[n][k]: 부호 없는 1종 스털링 수 (n 원소, k 사이클)
    c = [[0] * (N+1) for _ in range(N+1)]
    c[0][0] = 1

    for i in range(1, N+1):
        for j in range(1, i+1):
            c[i][j] = c[i - 1][j - 1] + (i - 1) * c[i - 1][j]

    num = sum(c[N][k] for k in range(1, M+1))
    den = math.factorial(N)

    g = math.gcd(num, den)

    ans = f"{num // g}/{den // g}"

    return ans


N, M = map(int, input().split())
M = min(M, N)   # 안전 장치

print(solve())
