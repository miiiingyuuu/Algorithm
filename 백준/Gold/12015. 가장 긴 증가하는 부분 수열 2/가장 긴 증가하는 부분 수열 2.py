import sys

input = sys.stdin.readline


def solve(lst, num):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return left


n = int(input())
sequences = list(map(int, input().split()))

lst = []

for num in sequences:
    if not lst or num > lst[-1]:
        lst.append(num)
    else:
        current = solve(lst, num)
        lst[current] = num

print(len(lst))