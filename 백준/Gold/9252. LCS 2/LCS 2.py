import sys

input = sys.stdin.readline


def solve(str1, str2):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs_length = dp[n][m]

    if lcs_length == 0:
        return lcs_length, ""

    lcs_str = [""] * lcs_length
    i, j = n, m
    idx = lcs_length - 1

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str[idx] = str1[i-1]
            i -= 1
            j -= 1
            idx -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs_length, ''.join(lcs_str)


str1 = input().strip()
str2 = input().strip()
n = len(str1)
m = len(str2)

length, result = solve(str1, str2)

print(length)
if length > 0:
    print(result)