import sys

input = sys.stdin.readline


n = int(input())
sequences = list(map(int, input().split()))

dp = [1] * n    # 각 위치까지의 수열 길이 저장
lst = [-1] * n  # 실제 답의 수열을 추적하기 위한 인덱스 저장

# sequnces[i]보다 작고 dp[i]가 연속인지 확인, 해당하는 인덱스를 lst에 저장
for i in range(1, n):
    for j in range(i):
        if sequences[j] < sequences[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            lst[i] = j

# 최대 길이 수열 얻기
max_len = max(dp)
idx = dp.index(max_len)

# 해당하는 최대 길이 수열 알아내기
ans = []
while idx != -1:
    ans.append(sequences[idx])
    idx = lst[idx]

# 역순으로 받아왔으니 뒤집기
ans.reverse()

print(max_len)
print(*ans)