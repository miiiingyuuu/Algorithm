import sys
from itertools import permutations

input = sys.stdin.readline


def solve(now):
    global ans

    if now[0] == '0':
        return

    tmp_now = "".join(now)
    int_num = int(tmp_now)

    if int_num < int(B):
        ans = max(ans, int_num)


A, B = input().split()

ans = -float('inf')

for perm in permutations(A, len(A)):
    solve(perm)

print(ans if ans != -float('inf') else -1)
