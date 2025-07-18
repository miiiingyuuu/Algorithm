import sys

input = sys.stdin.readline

'''
그냥 순열이 아니라 부분순열이라는걸 알아야했다! -> 문제의 lst는 일단 수열로 주어짐
ex) 1, 2, 3, 4, 5으로 순열로 나와도 연속으로 커지는 수만 계산하는게 아니라 연속이 아닌 숫자도 포함하여 부분수열을 구해야함
'''


def solve(idx, tmp_sum):
    global cnt

    if idx >= n:
        return

    tmp_sum += nums[idx]

    if tmp_sum == s:
        cnt += 1

    # 현재 idx를 선택하고 다음으로 넘어가는 경우
    solve(idx + 1, tmp_sum)

    # 현재 idx를 선택하지 않고 다음으로 넘어가는 경우
    solve(idx + 1, tmp_sum - nums[idx])


n, s = map(int, input().split())    # s: tar
nums = list(map(int, input().split()))

cnt = 0

solve(0, 0)   # 시작 idx, tmp_sum

print(cnt)
