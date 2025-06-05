import sys
from itertools import combinations

input = sys.stdin.readline

'''
방법1: 조합으로 가능한 경우를 확인해서 모음이 포함되어있다면 출력
방법2: 백트래킹으로 가능한 조합을 생각해서 가능한지 체크
백트래킹 연습을 위해 방법2로 진행
'''


# 최소 하나의 모음과 두 개의 자음이 필요
def check(lst):
    v_cnt = 0

    for i in lst:
        if i in vowel:
            v_cnt += 1

    c_cnt = len(lst) - v_cnt

    return v_cnt >= 1 and c_cnt >= 2


def solve(start, lst):
    if len(lst) == l:
        if check(lst):
            print("".join(lst))
        return

    for i in range(start, c):
        lst.append(words[i])
        solve(i + 1, lst)
        lst.pop()


l, c = map(int, input().split())  # l: 암호길이, c: 단어 갯수
words = list(input().split())
words.sort()

vowel = ['a', 'e', 'i', 'o', 'u']

solve(0, [])  # 시작 위치, 확인해볼 문자열
