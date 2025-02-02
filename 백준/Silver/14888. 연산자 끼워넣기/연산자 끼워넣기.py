import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_ans = -int(1e9)
min_ans = int(1e9)


def dfs(add, sub, mul, div, sum_val, idx):
    global max_ans, min_ans
    if idx == N:
        max_ans = max(max_ans, sum_val)
        min_ans = min(min_ans, sum_val)
        return

    if add:
        dfs(add-1, sub, mul, div, sum_val + lst[idx], idx+1)
    if sub:
        dfs(add, sub-1, mul, div, sum_val - lst[idx], idx+1)
    if mul:
        dfs(add, sub, mul-1, div, sum_val * lst[idx], idx+1)
    if div:
        dfs(add, sub, mul, div-1, int(sum_val / lst[idx]), idx+1)


dfs(add, sub, mul, div, lst[0], 1)
print(max_ans)
print(min_ans)