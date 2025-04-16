import sys

input = sys.stdin.readline


def solve():
    if w <= 2:
        return 0

    ans = 0
    left = 0
    right = w-1
    left_max = block_h[left]
    right_max = block_h[right]

    while left < right:
        if block_h[left] < block_h[right]:
            left += 1
            if block_h[left] < left_max:
                ans += left_max - block_h[left]
            else:
                left_max = block_h[left]
        else:
            right -= 1
            if block_h[right] < right_max:
                ans += right_max - block_h[right]
            else:
                right_max = block_h[right]

    return ans


h, w = map(int, input().split())
block_h = list(map(int, input().split()))

print(solve())