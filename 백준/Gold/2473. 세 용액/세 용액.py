import sys
from collections import deque
input = sys.stdin.readline


def solve():
    closest_sum = float('inf')
    result = []

    for i in range(n-2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = solutions[i] + solutions[left] + solutions[right]
            if abs(closest_sum) > abs(current_sum):
                closest_sum = current_sum
                result = [solutions[i], solutions[left], solutions[right]]

            if current_sum < 0:
                left += 1
            elif current_sum > 0:
                right -= 1
            else:
                return [solutions[i], solutions[left], solutions[right]]

    return result


n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

result = solve()

print(*result)