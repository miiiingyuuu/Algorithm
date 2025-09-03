import sys

input = sys.stdin.readline

'''
1. 가장 왼쪽의 계란 들기
2. 깨지지 않은 계란 중에 하나 치기 -> 손에 든 계란 깨졌으면 끝 or 이후 손에 든 계란 원래 자리에 놓기
3. 들었던 계란의 오른쪽 계란을 골라서 깨기 -> 이전에 들었던게 가장 마지막이면 끝
'''


def solve(idx):
    global ans

    # 가장 오른쪽 계란을 치고 난 이후(N)이면 끝
    if idx == N:
        broken = sum(1 for s, _ in eggs if s <= 0)
        ans = max(ans, broken)
        return

    if eggs[idx][0] <= 0:
        solve(idx+1)
        return

    # 현재 계란으로 칠 수 있는 대상이 있는지 확인
    possible = False
    for i in range(N):
        # 본인이거나, 내구도가 0인 계란은 칠 수 없음
        if i == idx or eggs[i][0] <= 0:
            continue

        possible = True

        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        solve(idx + 1)
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]

    # 칠 수 없는 대상이 없으므로 다음 번호로 넘어가기
    if not possible:
        solve(idx + 1)


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

ans = -float('inf')

solve(0) # idx

print(ans)
