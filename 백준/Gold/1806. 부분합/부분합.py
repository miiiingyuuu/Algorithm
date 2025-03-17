import sys

input = sys.stdin.readline


def solve():
    left = 0
    current_sum = 0
    ans = 1e999999

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= s and left <= right:
            ans = min(ans, right - left + 1)
            current_sum -= nums[left]
            left += 1

    if ans == 1e99999:
        return 0
    else:
        return ans


n, s = map(int, input().split())
nums = list(map(int, input().split()))
print(solve())