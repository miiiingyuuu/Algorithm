import sys

input = sys.stdin.readline


def lower_bound(arr, x):
    ll, rr = 0, len(arr)
    while ll < rr:
        mid = (ll + rr) // 2
        if arr[mid] < x:
            ll = mid + 1
        else:
            rr = mid

    return ll


def upper_bound(arr, x):
    ll, rr = 0, len(arr)
    while ll < rr:
        mid = (ll + rr) // 2
        if arr[mid] <= x:
            ll = mid + 1
        else:
            rr = mid

    return ll


N, M = map(int, input().split())    # N: 점의 개수, M: 선분의 개수
points = list(map(int, input().split()))
points.sort()

for _ in range(M):
    l, r = map(int, input().split())
    left = lower_bound(points, l)
    right = upper_bound(points, r)
    print(right - left)
