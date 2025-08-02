import sys

input = sys.stdin.readline


def solve():
    return (N * M) - 1


N, M = map(int, input().split())

print(solve())
