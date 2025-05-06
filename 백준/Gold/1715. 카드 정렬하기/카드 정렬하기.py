import sys
import heapq
input = sys.stdin.readline


def solve():
    heapq.heapify(cards)
    ans = 0

    while len(cards) > 1:
        tmp1 = heapq.heappop(cards)
        tmp2 = heapq.heappop(cards)

        sum_tmp = tmp1 + tmp2
        ans += sum_tmp

        heapq.heappush(cards, sum_tmp)

    return ans


n = int(input())
cards = [int(input()) for _ in range(n)]

print(solve())