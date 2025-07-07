import sys

input = sys.stdin.readline


'''
부분 문자열이란? 어떤 문자열에서 t가 연속으로 나타나는 것을 의미
dp[i][j] = words1의 i번째 단어와 words2 j번째 단어가 공통적으로 해당되는 문자열인지 확인하는 2차원 배열
같은 문자라면 dp[i-1][j-1] + 1을 통해 연속적으로 이전의 단어와도 같았는지 확인하며 가장 긴 공통 부분 문자열 확인 가능
'''


def solve():
    dp = [[0] * (m+1) for _ in range(n+1)]
    ans = 0

    # 2차원 배열 순회를 통해 연속된 문자열 찾고 계속 초기화 해주기
    for i in range(1, n+1):
        for j in range(1, m+1):
            if words1[i-1] == words2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                ans = max(ans, dp[i][j])

    return ans


words1 = list(input().strip())
n = len(words1)
words2 = list(input().strip())
m = len(words2)

print(solve())
