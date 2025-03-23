import sys

input = sys.stdin.readline


def solve(arr, tar):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == tar:
            return True
        elif arr[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1

    return False


n = int(input())
sang_cards = list(map(int, input().split()))
m = int(input())
if_cards = list(map(int, input().split()))

sang_cards.sort()

result = []
for i in if_cards:
    if solve(sang_cards, i):
        result.append(1)
    else:
        result.append(0)

print(*result)