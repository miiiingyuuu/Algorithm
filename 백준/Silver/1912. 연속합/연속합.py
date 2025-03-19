import sys

input = sys.stdin.readline


def solve():
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, n):
        current_sum = max(nums[i], current_sum + nums[i])

        max_sum = max(max_sum, current_sum)

    return max_sum


n = int(input())
nums = list(map(int, input().split()))
print(solve())