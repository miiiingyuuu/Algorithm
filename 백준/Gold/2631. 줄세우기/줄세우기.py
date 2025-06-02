import sys

input = sys.stdin.readline

'''
가장 긴 증가하는 부분수열을 구하면 해당하는 부분수열은 오름차순으로 위치가 맞는 것이고,
해당하지 않는 숫자를 한번 씩 옮기면 정렬이 완료된다.
답은 전체 수 n에서 dp배열의 max 값을 뺀 값
'''


def solve():
    # 자기 자신만 포함하면 모두 길이가 1부터 시작
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if c_num[j] < c_num[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


n = int(input())
c_num = [int(input()) for _ in range(n)]

result = solve()
print(n - result)
