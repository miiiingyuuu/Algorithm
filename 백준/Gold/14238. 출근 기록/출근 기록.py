import sys
from collections import Counter

input = sys.stdin.readline

'''
A: 매일 출근 가능
B: 출근한 다음 날은 반드시 쉬어야 함
C: 출근한 다음날, 다다날은 반드시 쉬어야 함
무작위 출근기록 S에서 가능한 형태로 출력
5차원 행열 dp[a][b][c][p1][p2]로 풀어야된다... 0:A, 1:B, 2:C, 3:None / p1: 전날 출근자, p2: 전전날 출근자
'''


def solve(a, b, c, p1, p2):
    if a == 0 and b == 0 and c == 0:
        return True

    if (a, b, c, p1, p2) in memo:
        return memo[(a, b, c, p1, p2)]

    # A 선택
    if a > 0:
        if solve(a-1, b, c, 0, p1):
            path[(a, b, c, p1, p2)] = 'A'
            memo[(a, b, c, p1, p2)] = True
            return True

    # B 선택
    if b > 0 and p1 != 1:
        if solve(a, b-1, c, 1, p1):
            path[(a, b, c, p1, p2)] = 'B'
            memo[(a, b, c, p1, p2)] = True
            return True

    # C 선택
    if c > 0 and p1 != 2 and p2 != 2:
        if solve(a, b, c-1, 2, p1):
            path[(a, b, c, p1, p2)] = 'C'
            memo[(a, b, c, p1, p2)] = True
            return True

    memo[(a, b, c, p1, p2)] = False

    return False


S = input().strip()
cnt = Counter(S)

# A=0, B=1, C=2, NONE=3
NONE = 3
N = len(S)

memo = {}
# 경로 복원 딕셔너리
path = {}

if solve(cnt['A'], cnt['B'], cnt['C'], NONE, NONE):
    a, b, c = cnt['A'], cnt['B'], cnt['C']
    p1, p2 = NONE, NONE
    ans = []
    for _ in range(N):
        ch = path[(a, b, c, p1, p2)]
        ans.append(ch)
        if ch == 'A':
            a -= 1
            p1, p2 = 0, p1
        elif ch == 'B':
            b -= 1
            p1, p2 = 1, p1
        else:
            c -= 1
            p1, p2 = 2, p1
    print(''.join(ans))
else:
    print(-1)
    