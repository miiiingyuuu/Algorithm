import sys

input = sys.stdin.readline


def solve():
    ans = 0
    start = 1   # 최소 거리
    end = houses[-1] - houses[0]    # 최대 거리

    while start <= end:
        mid = (start + end) // 2    # mid만큼 간격을 두고 공유기 설치해보기

        cnt = 1   # 첫 번째 집 설치
        last_installed = houses[0]

        for i in range(1, n):
            if houses[i] - last_installed >= mid:
                cnt += 1
                last_installed = houses[i]

        # 공유기 설치 수가 목표보다 크다면 더 넓은 거리로 시도
        if cnt >= c:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans


n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

print(solve())