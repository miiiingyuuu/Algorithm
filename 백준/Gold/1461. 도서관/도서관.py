import sys

input = sys.stdin.readline

'''
음수, 양수 좌표를 각각 정렬 (멀리 있는 책부터 m만큼 묶어서 계산할 예정)
m권씩 묶어서 왕복 거리 계산 (m 중 먼 거리 * 2)
가장 먼 그룹은 왕복하지 않아도 됨, 마지막에 편도로 해야 최솟값
'''


def solve():
    # 음수, 양수 각각 나눠서 정렬
    left = []
    right = []
    for loc in locations:
        if loc > 0:
            right.append(loc)
        else:
            left.append(loc)

    left.sort()
    right.sort(reverse=True)

    distance = 0

    # 음수 방향 처리
    for i in range(0, len(left), m):
        distance += abs(left[i]) * 2

    # 양수 방향 처리
    for i in range(0, len(right), m):
        distance += right[i] * 2

    # 마지막으로 간 거리는 편도로 가니까 가장 멀리 간 거리는 한 번 빼주기
    farthest = 0
    if left and right:
        farthest = max(abs(left[0]), right[0])
    elif left:
        farthest = abs(left[0])
    elif right:
        farthest = right[0]

    distance -= farthest

    return distance


n, m = map(int, input().split())    # n: 책의 갯수, m: 들 수 있는 책의 갯수
locations = list(map(int, input().split()))


print(solve())