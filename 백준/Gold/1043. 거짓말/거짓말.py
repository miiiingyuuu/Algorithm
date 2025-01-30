import sys

input = sys.stdin.readline

N, M = map(int, input().split())
truth = set(input().split()[1:])  # 진실을 아는 사람들
parties = []
for _ in range(M):
    parties.append(set(input().split()[1:]))

# 진실을 아는 사람들이 있는 파티의 모든 사람들에게 진실이 전파됨
changed = True
while changed:
    changed = False
    for party in parties:
        # 파티에 진실을 아는 사람이 있다면
        if party & truth:  # 교집합 확인
            # 해당 파티의 모든 사람을 진실을 아는 사람에 추가
            if party - truth:  # 새로운 사람이 추가되는지 확인
                changed = True
                truth.update(party)

# 과장된 이야기를 할 수 있는 파티 계산
ans = 0
for party in parties:
    # 파티에 진실을 아는 사람이 없다면 과장 가능
    if not party & truth:  # 교집합이 없음
        ans += 1

print(ans)