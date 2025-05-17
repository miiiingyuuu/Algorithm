import sys

input = sys.stdin.readline


def solve():
    cnt = 0

    for tar in range(n):
        start, end = 0, n-1

        while start < end:
            # 자신은 제외
            if start == tar:
                start += 1
                continue
            if end == tar:
                end -= 1
                continue

            # tar이라면 cnt++
            if nums[start] + nums[end] == nums[tar]:
                cnt += 1
                break
            # tar이 크다면 start 옮기기, 아니면 end 옮기기
            elif nums[start] + nums[end] < nums[tar]:
                start += 1
            else:
                end -= 1

    return cnt


n = int(input())
nums = list(map(int, input().split()))
# good을 찾기 위해 정렬 후 start와 end를 더해보기
nums.sort()

print(solve())