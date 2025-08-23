import sys

input = sys.stdin.readline

'''
nums에서 초기값 2개로 -1, 0, 1을 하는 경우를 통해 차이값을 구한 후에
2번째 값의 차이가 동등하게 차이만큼 증가한다면 cnt 횟수를 갱신하는 방식으로 진행하면 될 듯?
'''


def solve():
    global ans

    # 값이 2개 이하라면 무조건 등차수열
    if N <= 2:
        return 0

    # 비교하는 2개의 값을 -1, 0, 1 중 하나를 해보기
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            tmp1 = nums[0] + i
            tmp2 = nums[1] + j
            # d: 차이가 d씩 나는지 확인용
            d = tmp2 - tmp1

            # 초기 변경 횟수 체크
            cnt = abs(i) + abs(j)
            possible = True

            for k in range(2, N):
                # d에 의한 다음 예상 값
                nxt_tmp = tmp1 + d * k
                # 차이가 1보다 크면 바꿔도 등차수열이 되지 않으므로 break
                if abs(nums[k] - nxt_tmp) > 1:
                    possible = False
                    break

                # 차이가 1이 넘게 나지 않는데, nxt_tmp가 아니라면 -1이나 +1을 해줘야 하므로 횟수가 증가
                if nums[k] != nxt_tmp:
                    cnt += 1

            if possible:
                ans = min(ans, cnt)

    return ans if ans != float('inf') else -1


N = int(input())
nums = list(map(int, input().split()))

ans = float('inf')

print(solve())
