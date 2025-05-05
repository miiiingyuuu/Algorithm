import sys

input = sys.stdin.readline

# 왼쪽에서 오른쪽으로 필요한 경우 스위치를 누르며 처리
# i-1번째 전구를 목표로 맞추기 위해서는 i번째 스위치는 반드시 눌러야함
# 첫 번쨰 스위치를 누르는 경우와 누르지 않는 경우로 나눠서 답을 얻기


def toggle(tmp, idx):
    for i in range(idx - 1, idx + 2):
        if 0 <= i < n:
            tmp[i] = '1' if tmp[i] == '0' else '0'


def solve():
    ans = float('inf')

    for press_first in [False, True]:
        tmp = now[:]
        cnt = 0
        if press_first:
            toggle(tmp, 0)
            cnt += 1

        for i in range(1, n):
            if tmp[i-1] != tar[i-1]:
                toggle(tmp, i)
                cnt += 1

        if tmp == tar:
            ans = min(ans, cnt)

    return ans if ans != float('inf') else -1


n = int(input())
now = list(input().strip())
tar = list(input().strip())

print(solve())