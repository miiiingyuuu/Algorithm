import sys

input = sys.stdin.readline


def solve(s, t):
    n = len(s)
    m = len(t)

    while n <= m:
        if s == t:
            return 1

        if t[-1] == 'A':
            t.pop()
            m -= 1
        elif t[-1] == 'B':
            t.pop()
            t.reverse()
            m -= 1

    return 0


s = list(input().strip())
t = list(input().strip())


print(solve(s, t))