import sys

input = sys.stdin.readline

'''
연산자마다 괄호를 치는 경우와 안치는 경우로 나눠 재귀적으로 탐색
괄호 없이 계산을 재귀적으로 한 이후에
괄호를 치고 계산하는 방식을 재귀적으로 진행
'''


def cal(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b


def solve(idx, cur_val):
    global ans

    # 수식의 끝에 도달했을 때 최댓값 갱신
    if idx >= len(exp):
        ans = max(ans, cur_val)
        return

    # 괄호 없이 계산
    next_val = cal(cur_val, exp[idx], int(exp[idx+1]))
    solve(idx + 2, next_val)

    # 괄호를 치는 경우에는 다음 연산자를 먼저 계산, 괄호를 치는 경우는 2번째 연산자가 나온 이후부터 의미가 있음
    if idx + 2 < len(exp):
        parentheses = cal(int(exp[idx+1]), exp[idx+2], int(exp[idx+3]))
        next_val = cal(cur_val, exp[idx], parentheses)
        # 2중 괄호는 불가능하므로 idx + 4부터 괄호쳐서 계산해보기
        solve(idx + 4, next_val)


n = int(input())
exp = list(input().strip())

ans = -float('inf')
solve(1, int(exp[0]))
print(ans)