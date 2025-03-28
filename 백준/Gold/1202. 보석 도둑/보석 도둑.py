import sys
import heapq
input = sys.stdin.readline

def solve():
    available_jewels = []

    ans = 0

    jewel_idx = 0

    for i in bags:
        while jewel_idx < n and jewels[jewel_idx][0] <= i:
            heapq.heappush(available_jewels, -jewels[jewel_idx][1])
            jewel_idx += 1

        if available_jewels:
            ans += -heapq.heappop(available_jewels)

    return ans


n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort()
bags.sort()

print(solve())