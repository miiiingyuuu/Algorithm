import sys

input = sys.stdin.readline

'''
주어진 문자열을 문제에 맞게 빈 n*n 행렬에 입력을 한 이후에
백트래킹으로 가장 낮은 숫자 -10부터 시작해서 10까지 입력을 하면서 매번 조건을 만족하면 넣고, 아니면 빼는 식으로 진행
'''


def is_valid(i):
    total = 0
    for j in range(i, -1, -1):
        total += result[j]
        arr_char = arr[j][i]
        if arr_char == '+' and total <= 0:
            return False
        elif arr_char == '-' and total >= 0:
            return False
        elif arr_char == '0' and total != 0:
            return False

    return True


def solve(depth):
    if depth == n:
        print(' '.join(map(str, result)))
        exit(0)

    for i in range(-10, 11):
        result[depth] = i
        if is_valid(depth):
            solve(depth + 1)


n = int(input())
s = list(input().strip())
arr = [[None] * n for _ in range(n)]

idx = 0
for i in range(n):
    for j in range(i, n):
        arr[i][j] = s[idx]
        idx += 1

result = [0] * n

solve(0)