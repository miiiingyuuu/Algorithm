import sys

input = sys.stdin.readline


n = int(input())
expectations = []
for i in range(n):
    num = int(input())
    expectations.append(num)
expectations.sort()

ans = 0
for j in range(1, n+1):
    ans += abs(expectations[j-1] - j)

print(ans)