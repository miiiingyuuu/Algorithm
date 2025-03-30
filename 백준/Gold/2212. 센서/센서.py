import sys

input = sys.stdin.readline


def solve():
    if k >= n:
        return 0
    else:
        distances = [sensors[i+1] - sensors[i] for i in range(n-1)]

        distances.sort()

        result = sum(distances[:n-k])

        return result


n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

print(solve())