import sys

input = sys.stdin.readline


N, C = map(int, input().split())
M = int(input())
boxes_info = []
for i in range(M):
    a, b, w = map(int, input().split())
    boxes_info.append((a, b, w))

boxes_info.sort(key=lambda x: x[1])

box_available = [C] * (N + 1)
ans = 0

# 정렬된 박스 정보를 순회
for s, d, box_cnt in boxes_info:
    # 현재 배송 경로(s~d)에서 실을 수 있는 최대 박스 수 계산
    min_val = box_cnt

    # 출발지부터 도착지 직전까지의 구간에서 최소 용량 찾기
    # 이 경로에서 실을 수 있는 박스 수는 경로 상 가장 적은 용량으로 제한됨
    for i in range(s, d):
        min_val = min(min_val, box_available[i])

    # 출발지부터 도착지 직전까지의 모든 구간에서 용량 감소
    # 박스가 트럭에 실려 있는 동안은 해당 구간의 용량을 차지함
    for j in range(s, d):
        box_available[j] -= min_val

    ans += min_val

print(ans)