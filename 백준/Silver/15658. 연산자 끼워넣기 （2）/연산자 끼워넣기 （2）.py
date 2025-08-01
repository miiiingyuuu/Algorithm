import sys

input = sys.stdin.readline


def solve(add, sub, mul, div, tmp_sum, depth):
    global max_ans, min_ans

    if depth == n:
        max_ans = max(max_ans, tmp_sum)
        min_ans = min(min_ans, tmp_sum)
        return

    if add:
        solve(add - 1, sub, mul, div, tmp_sum + nums[depth], depth + 1)
    if sub:
        solve(add, sub - 1, mul, div, tmp_sum - nums[depth], depth + 1)
    if mul:
        solve(add, sub, mul - 1, div, tmp_sum * nums[depth], depth + 1)
    if div:
        solve(add, sub, mul, div - 1, int(tmp_sum / nums[depth]), depth + 1)


n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_ans = -float('inf')
min_ans = float('inf')

solve(add, sub, mul, div, nums[0], 1)
print(max_ans)
print(min_ans)
