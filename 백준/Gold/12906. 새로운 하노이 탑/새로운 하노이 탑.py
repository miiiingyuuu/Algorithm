import sys
from collections import deque

input = sys.stdin.readline

'''
A: 0, B: 1, C: 2
'''


def is_complete(status):
    # A탑에는 A만, B타워에는 B만, C타워에는 C만 있다면 끝
    for i, rod in enumerate(status):
        tar = "ABC"[i]
        if any(ring != tar for ring in rod):
            return False

    return True


def solve():
    # 해당 상태의 타워를 방문했는지 체크하는 visited
    visited = set()
    q = deque()
    q.append((tower_status, 0)) # 현 상태, 횟수
    visited.add(tower_status)

    while q:
        curr_status, cnt = q.popleft()

        if is_complete(curr_status):
            return cnt

        # 막대기 순서
        for i in range(3):
            if not curr_status[i]:
                continue

            # 다른 막대기로 이동할 수 있는지 확인
            for j in range(3):
                if i == j:
                    continue

                new_status = list(map(list, curr_status))
                ring = new_status[i].pop()
                new_status[j].append(ring)
                new_status_tuple = tuple(tuple(rod) for rod in new_status)
                if new_status_tuple not in visited:
                    visited.add(new_status_tuple)
                    q.append((new_status_tuple, cnt + 1))

    return -1


a = input().split()
a_line = tuple(a[1]) if int(a[0]) > 0 else ()
b = input().split()
b_line = tuple(b[1]) if int(b[0]) > 0 else ()
c = input().split()
c_line = tuple(c[1]) if int(c[0]) > 0 else ()

tower_status = (a_line, b_line, c_line)

print(solve())
