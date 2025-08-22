import sys

input = sys.stdin.readline


def solve(idx, cnt, curr, min_val, max_val):
    global ans

    if idx == n:
        # 문제를 내는 조건 체크: 2문제 이상, min, max, max-min 값 확인
        if cnt >= 2 and l <= curr <= r and max_val - min_val >= x:
            ans += 1
        return

    # 현재 문제 선택
    solve(idx + 1, cnt + 1, curr + a[idx], min(min_val, a[idx]), max(max_val, a[idx]))

    # 현재 문제 선택 x
    solve(idx + 1, cnt, curr, min_val, max_val)


n, l, r, x = map(int, input().split())  # n: 문제 수, l: max 난이도, r: min 난이도, x: abs(l-r)
a = list(map(int, input().split()))

ans = 0

solve(0, 0, 0, 1e999999, -1e999999) # idx, cnt, curr, min, max

print(ans)
