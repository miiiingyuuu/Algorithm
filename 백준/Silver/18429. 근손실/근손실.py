import sys
from itertools import permutations
input = sys.stdin.readline


def solve(order):
    cur_weight = 500

    for kit in order:
        cur_weight += kits[kit]
        cur_weight -= k
        if cur_weight < 500:
            return False

    return True


n, k = map(int, input().split())
kits = list(map(int, input().split()))

cnt = 0
for order in permutations(range(n)):
    if solve(order):
        cnt += 1

print(cnt)