import sys

input = sys.stdin.readline


def bitonic_subsequence(N, A):
    increase = [1] * N
    decrease = [1] * N

    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                increase[i] = max(increase[i], increase[j] + 1)

    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            if A[i] > A[j]:
                decrease[i] = max(decrease[i], decrease[j] + 1)

    ans = 0
    for i in range(N):
        ans = max(ans, increase[i] + decrease[i] - 1)

    return ans


N = int(input())
A = list(map(int, input().split()))

result = bitonic_subsequence(N, A)
print(result)