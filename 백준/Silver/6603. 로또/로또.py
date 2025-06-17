import sys
from itertools import combinations

input = sys.stdin.readline


while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0 and len(nums) == 1:
        break

    for combination in combinations(nums[1:], 6):
        print(*combination)
    print(" ")
