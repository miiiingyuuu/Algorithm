import sys

input = sys.stdin.readline


def mod_inverse(b, mod):
    return pow(b, mod - 2, mod)


def calculate_expectation():
    MOD = 1000000007

    M = int(input())
    result = 0

    for _ in range(M):
        N, S = map(int, input().split())

        inv_N = mod_inverse(N, MOD)
        result = (result + (S * inv_N) % MOD) % MOD

    return result


if __name__ == "__main__":
    print(calculate_expectation())
