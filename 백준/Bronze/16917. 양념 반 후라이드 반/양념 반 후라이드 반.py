import sys

input = sys.stdin.readline


def solve():
    # 사야하는 마리 수가 같다면 둘 중에 최소값으로
    if x == y:
        return min((a * x) + (b * y), c * (x * 2))

    # 그냥 한 마리 씩 사는 경우
    tmp1 = (a * x) + (b * y)

    # 반 마리를 x, y 중 (최소값 * 2) 그리고 남은 마리 수만큼 그 치킨 사기 / 최소 마리 수가 x, y이므로 넘어도 상관 없네
    min_val = min(x, y)
    max_val = max(x, y)

    if x - y > 0:
        tmp_val = a * (x - y)
    else:
        tmp_val = b * (y - x)

    tmp2 = min((c * 2) * min_val + tmp_val, (c * 2) * max_val)

    return min(tmp1, tmp2)


a, b, c, x, y = map(int, input().split())

print(solve())
