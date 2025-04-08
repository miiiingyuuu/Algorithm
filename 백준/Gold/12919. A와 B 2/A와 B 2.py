import sys

input = sys.stdin.readline


def solve(t):
    if s == t:
        return 1

    if len(t) < len(s):
        return 0

    result = 0
    if t[-1] == 'A':
        result |= solve(t[:-1])

    if t[0] == 'B':
        result |= solve(t[1:][::-1])

    return result


s = input().strip()
t = input().strip()

print(solve(t))