import sys

input = sys.stdin.readline


'''
크리 키보드는 아래의 4가지 행동을 수행
1. 화면에 A를 출력
2. 화면을 전체 선택
3. 전체 선택한 내용을 버퍼에 복사
4. 출력된 문자열의 바로 뒤에 버퍼의 내용을 붙여넣기
총 n번 눌러서 a의 개수가 최대가 되는 경우
dp[i]: i번 눌러서 가능한 A의 최대 개수
'''


def solve():
    # 생각해보면 화면을 전체 선택 -> 복사 -> 붙여넣기의 경우에 3번 클릭이 소모가 되므로 최소 6번의 클릭이 있어야 AAA를 복사하여 붙여넣기가 가능
    if n < 7:
        return n

    # dp[i]: i번 눌러서 가능한 A의 최대 개수
    dp = [0] * (n + 1)

    for i in range(1, 7):
        dp[i] = i

    # 7번째 클릭 이후로 선택 -> 복사 -> 붙여넣기를 어떻게 하는지에 따라 최대값 계산하기
    for i in range(7, n+1):
        for j in range(i - 3, 0, -1):
            # j 시점에서 복사 시작, (i - j - 1)번 붙여넣기
            dp[i] = max(dp[i], dp[j] * (i - j - 1))

    return dp[n]


n = int(input())

print(solve())
