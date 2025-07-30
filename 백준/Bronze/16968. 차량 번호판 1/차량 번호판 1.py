import sys

input = sys.stdin.readline


def solve():
    ans = 1
    prev = ''

    for word in pattern:
        if word == 'c':
            tmp = 26
        else:
            tmp = 10

        if word == prev:
            tmp -= 1

        ans *= tmp
        prev = word

    return ans


pattern = input().strip()

print(solve())
