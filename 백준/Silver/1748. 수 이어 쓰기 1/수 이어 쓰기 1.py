import sys

input = sys.stdin.readline

'''
digit의 수 만큼 (9 * (10*(n-1))) 곱하는 수가 각 자리 수 만큼의 최대 자리수
이전 자리 수까지 갯수를 구하고, 현재 자리 수에서 남은 자리수를 계산해서 답 구하기
'''


def solve():
    digit = 1
    start = 1
    ans = 0

    while start * 10 <= n:
        cnt = 9 * start
        ans += cnt * digit
        digit += 1
        start *= 10

    ans += (n - start + 1) * digit

    return ans


n = int(input())

print(solve())