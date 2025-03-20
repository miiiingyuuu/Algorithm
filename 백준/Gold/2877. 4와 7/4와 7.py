import sys

input = sys.stdin.readline


def solve(n):
    binary = bin(n+1)[3:]
    result = ''.join('4' if b == '0' else '7' for b in binary)

    return result


n = int(input())
print(solve(n))