import sys

input = sys.stdin.readline


def solve(fold):
    n = len(fold)

    if n == 1:
        return True

    mid = n // 2
    left_half = fold[:mid]
    right_half = fold[mid+1:]

    for i in range(len(left_half)):
        if left_half[i] == right_half[len(right_half) - 1 - i]:
            return False

    return solve(left_half)


t = int(input())
for tc in range(t):
    fold = list(map(int, input().strip()))

    if solve(fold):
        print("YES")
    else:
        print("NO")