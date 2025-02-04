import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
time = 0
truck_weights = deque(trucks)
current_weight = 0

while truck_weights or current_weight > 0:
    current_weight -= bridge[0]
    bridge.popleft()

    if truck_weights:
        if current_weight + truck_weights[0] <= l:
            truck = truck_weights.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            bridge.append(0)
    else:
        bridge.append(0)

    time += 1

print(time)