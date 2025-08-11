import sys

input = sys.stdin.readline


def solve(start):
    tmp_lst = [start]

    while len(tmp_lst) < N:
        curr = tmp_lst[-1]
        if curr * 2 in nums and (len(tmp_lst) == 1 or curr * 2 != tmp_lst[-2]):
            tmp_lst.append(curr * 2)
        elif curr % 3 == 0 and curr // 3 in nums and (len(tmp_lst) == 1 or curr // 3 != tmp_lst[-2]):
            tmp_lst.append(curr // 3)
        else:
            break

    return tmp_lst


N = int(input())
nums = list(map(int, input().split()))

for num in nums:
    result = solve(num)
    if len(result) == N:
        print(*result)
        break
