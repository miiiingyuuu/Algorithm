import sys

input = sys.stdin.readline

'''
해당하는 e, s, m을 뺀 년도를 각각 15, 28, 19로 나눈 값의 나머지가 0인 년도가 각 e, s, m을 만족하는 답
'''

def solve():
    ans = 1
    while True:
        if (ans - e) % 15 == 0 and (ans - s) % 28 == 0 and (ans - m) % 19 == 0:
            return ans
        ans += 1


e, s, m = map(int, input().split())

print(solve())