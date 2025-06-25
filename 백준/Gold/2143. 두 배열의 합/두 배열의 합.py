import sys
from collections import Counter

input = sys.stdin.readline

'''
배열의 누적합을 미리 구하고 각 누적합의 합이 t인것을 만족하는 i, j의 쌍의 갯수를 얻기
'''


def get_sums(lst):
    n = len(lst)
    sum_lst = []
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += lst[j]
            sum_lst.append(total)

    return sum_lst


def solve(t, a, b):
    # lst1과 lst2의 모든 부 배열 합 구하기
    sum_lst1 = get_sums(a)
    sum_lst2 = get_sums(b)

    # lst1의 부배열 합 빈도수 세기
    counter_lst1 = Counter(sum_lst1)

    # lst2의 부배열 합과 lst1의 것들의 합이 t가 되는 쌍 개수 세기(t - sum_lst2가 sum_lst1의 값이 되면 만족함)
    cnt = 0
    for i in sum_lst2:
        cnt += counter_lst1[t - i]

    return cnt


t = int(input())
n1 = int(input())
lst1 = list(map(int, input().split()))
n2 = int(input())
lst2 = list(map(int, input().split()))

print(solve(t, lst1, lst2))
