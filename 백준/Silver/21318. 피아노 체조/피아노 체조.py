import sys

input = sys.stdin.readline


N = int(input())
difficulty = list(map(int, input().split()))
Q = int(input())

not_play = [0] * N
for i in range(1, N):
    if difficulty[i-1] > difficulty[i]:
        not_play[i-1] = 1

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + not_play[i-1]

for _ in range(Q):
    start, end = map(int, input().split())
    result = prefix_sum[end-1] - prefix_sum[start-1]
    print(result)
