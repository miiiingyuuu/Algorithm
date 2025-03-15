import sys

input = sys.stdin.readline


n = int(input())
solutions = list(map(int, input().split()))

left = 0
right = n - 1

min_ans = 1e999999
ans = []

while left < right:
    current_sum = solutions[left] + solutions[right]

    if abs(current_sum) < min_ans:
        min_ans = abs(current_sum)
        ans = [solutions[left], solutions[right]]

    if current_sum < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])


