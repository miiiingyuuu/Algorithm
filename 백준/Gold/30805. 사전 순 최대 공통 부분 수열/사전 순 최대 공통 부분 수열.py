import sys

input = sys.stdin.readline


def sol(arr1, arr2):
    # 두 배열 중 하나라도 비어 있으면 빈 리스트 반환
    if (not arr1) or (not arr2):
        return []

    # arr1과 arr2에서 각각 가장 큰 값과 그 인덱스를 찾음
    tmp1, tmp2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(tmp1), arr2.index(tmp2)

    # 두 값이 같으면 현재 값과 나머지 부분의 결과를 합쳐서 반환
    if tmp1 == tmp2:
        return [tmp1] + sol(arr1[idx1 + 1:], arr2[idx2 + 1:])
    # tmp1이 더 크면 arr1에서 제거하고 재귀 호출
    elif tmp1 > tmp2:
        arr1.pop(idx1)
        return sol(arr1, arr2)
    # tmp2가 더 크면 arr2에서 제거하고 재귀 호출
    else:
        arr2.pop(idx2)
        return sol(arr1, arr2)


n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# 함수 호출
ans = sol(arr1, arr2)

# 결과 출력
print(len(ans))
if ans:
    print(*ans)