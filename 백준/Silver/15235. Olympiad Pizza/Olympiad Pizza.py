import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
pizza = list(map(int, input().split()))

result = [0] * n

# 참가자의 idx와 남은 피자 수
q = deque([(i, pizza[i]) for i in range(n)])

t = 0
while q:
    t += 1
    idx, pizza_left = q.popleft()

    pizza_left -= 1

    if pizza_left == 0:
        result[idx] = t
    else:
        q.append((idx, pizza_left))

print(*result)