import sys

input = sys.stdin.readline


def solve(expr, num, n, result):
    if num > n:
        if eval(expr.replace(' ', '')) == 0:
            result.append(expr)
        return

    solve(expr + '+' + str(num), num + 1, n, result)
    solve(expr + '-' + str(num), num + 1, n, result)
    solve(expr + ' ' + str(num), num + 1, n, result)


t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    solve('1', 2, n, result)
    result.sort()
    for i in result:
        print(i)
    print()