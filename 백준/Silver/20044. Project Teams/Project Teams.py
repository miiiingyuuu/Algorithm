import sys

input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
w.sort()

ans = []

for i in range(len(w) // 2):
    x = w[i] + w[-i-1]
    ans.append(x)

print(min(ans))
