import sys
import heapq
input = sys.stdin.readline


n = int(input())
nums = [int(input()) for _ in range(n)]

max_heap = []   # 중간값 이하
min_heap = []   # 중간값 초과

result = []

for i in range(n):
    # max_heap에 먼저 삽입
    heapq.heappush(max_heap, -nums[i])

    # max_heap의 0번째를 min_heap으로 이동
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # min_heap의 갯수가 더 많아졌다면 max_heap에 다시 넣기
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # 중간값은 max_heap의 0번째 값
    result.append(-max_heap[0])

for ans in result:
    print(ans)