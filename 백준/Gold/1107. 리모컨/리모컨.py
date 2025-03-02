import sys

input = sys.stdin.readline


def solve(target, broken_buttons):
    # +/- 버튼만 사용하여 가는 경우
    ans = abs(target - 100)

    for channel in range(1000001):
        channel_str = str(channel)
        valid = True

        for i in channel_str:
            if int(i) in broken_buttons:
                valid = False
                break

        # 고장난 버튼이 포함되지 않는 숫자의 경우 버튼 누를 최수 횟수 계산
        if valid:
            tmp_ans = len(channel_str) + abs(channel - target)
            ans = min(ans, tmp_ans)

    return ans


tar_channel = int(input())
N = int(input())
broken_buttons = set()
if N > 0:
    broken_buttons = set(map(int, input().split()))

print(solve(tar_channel, broken_buttons))