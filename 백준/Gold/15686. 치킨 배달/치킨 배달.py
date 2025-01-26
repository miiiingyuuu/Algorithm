import sys
input = sys.stdin.readline  # 입력 속도 향상을 위한 설정

# N x N 크기의 도시와 최대 치킨집 개수 M 입력
n, m = map(int, input().split())
# 도시 정보를 2차원 리스트로 입력 (0: 빈칸, 1: 집, 2: 치킨집)
graph = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)  # 최소 치킨 거리를 저장할 변수, 초기값은 큰 수로 설정
house = []      # 집의 좌표를 저장할 리스트
chicken = []    # 치킨집의 좌표를 저장할 리스트

# 도시를 순회하며 집과 치킨집의 좌표 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

arr = []  # 선택된 치킨집의 인덱스를 저장할 리스트

def back(num, cnt):
    global ans
    # 치킨집 개수를 초과하면 종료
    if num > len(chicken):
        return

    # M개의 치킨집을 선택했을 때
    if cnt == m:
        result_tot = 0  # 도시의 치킨 거리
        # 각 집에 대해 가장 가까운 치킨집과의 거리 계산
        for hx, hy in house:
            min_check = int(1e9)  # 현재 집의 최소 치킨 거리
            for idx in arr:
                cx, cy = chicken[idx]
                # 맨해튼 거리 계산하여 최소값 갱신
                min_check = min(min_check, abs(hx - cx) + abs(hy - cy))

            result_tot += min_check  # 도시의 치킨 거리에 추가

        # 최소 치킨 거리 갱신
        ans = min(result_tot, ans)
        return

    # 백트래킹을 통한 치킨집 선택
    arr.append(num)  # 현재 치킨집 선택
    back(num + 1, cnt + 1)  # 다음 치킨집 선택
    arr.pop()  # 현재 치킨집 선택 취소
    back(num + 1, cnt)  # 현재 치킨집 선택하지 않고 다음으로
    return ans

print(back(0, 0))  # 백트래킹 시작하여 최소 치킨 거리 출력