import sys
from itertools import combinations
from collections import Counter

input = sys.stdin.readline

'''
최대 n=40에서 부분수열의 합이 s가 되는 경우의 수를 구하기는 완전탐색은 불가
1. 수열을 두 부분으로 나누어 각각의 부분집합의 합을 구함
2. 한 쪽의 부분집합의 합과 다른 쪽 부분집합의 합을 조합해서 s를 만드는 경우의 수를 셈
3. 정렬 + 이진 탐색으로 개수 세기
'''


def subsequence_sums(arr):
    result = []
    n = len(arr)
    # 가능한 부분수열의 합의 경우를 result 배열에 반환
    for i in range(1, n+1):
        for comb in combinations(arr, i):
            result.append(sum(comb))

    return result


def solve():
    mid = n // 2
    left = nums[:mid]
    right = nums[mid:]

    # 좌, 우 부분수열 합의 경우를 구하기
    left_sums = subsequence_sums(left)
    right_sums = subsequence_sums(right)

    right_counter = Counter(right_sums)

    cnt = 0
    # left_sums에서 가능한 경우 l에서 s - l이 right_sums이 되는 경우를 찾으면 l + r = s가 성립됨
    for l in left_sums:
        cnt += right_counter[s - l]

    # 부분수열이 하나만 쓰는 경우도 고려
    cnt += left_sums.count(s)
    cnt += right_sums.count(s)

    return cnt


n, s = map(int, input().split())    # n: 개수, s: target
nums = list(map(int, input().split()))
nums.sort()

print(solve())
