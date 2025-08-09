import sys

input = sys.stdin.readline

'''
해당하는 추의 무게를 알기 위해서는 존재하는 추와 tar_추의 차이가 0이 되어야 함
추를 왼쪽, 오른쪽, 사용 안하는 경우로 나눔
'''


def solve():
    MAX_W = 40000

    # dp[i][j]: i번째까지의 추를 썼을때, 무게 차 j를 만들 수 있는지 확인
    dp = [[False] * (MAX_W + 1) for _ in range(n + 1)]

    dp[0][0] = True  # 아무 추도 사용하지 않았다면 차이는 0

    for i in range(1, n + 1):
        # 사용할 추
        w = weights[i - 1]
        for j in range(MAX_W + 1):
            if dp[i - 1][j]:
                # 추를 사용하지 않는 경우 (무게 차이 변화 없음)
                dp[i][j] = True

                # 왼쪽에 올리는 경우 (무게 차이 증가)
                if j + w <= MAX_W:
                    dp[i][j + w] = True

                # 오른쪽에 올리는 경우 (무게 차이 감소)
                dp[i][abs(j - w)] = True

    # 결과 리스트에 담기
    result = []
    for tar in tar_weights:
        if tar <= MAX_W and dp[n][tar]:
            result.append("Y")
        else:
            result.append("N")

    return result


n = int(input())
weights = list(map(int, input().split()))
m = int(input())
tar_weights = list(map(int, input().split()))

print(" ".join(solve()))
