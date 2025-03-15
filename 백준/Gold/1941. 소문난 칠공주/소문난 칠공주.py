import sys
from collections import deque
input = sys.stdin.readline


def is_connected(positions):
    visited = set()
    q = deque([positions[0]])
    visited.add(positions[0])

    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            new_pos = (nr, nc)

            if new_pos in positions and new_pos not in visited:
                visited.add(new_pos)
                q.append(new_pos)

    return len(visited) == 7


def solve(current_positions, next_idx, s_count):
    global result

    if len(current_positions) == 7:
        if s_count >= 4:
            if is_connected(current_positions):
                result += 1
        return

    if next_idx == 25 or len(current_positions) + (25 - next_idx) < 7 or s_count + (7 - len(current_positions)) < 4:
        return

    r, c = next_idx // 5, next_idx % 5
    is_s = 1 if board[r][c] == 'S' else 0

    current_positions.append((r, c))
    solve(current_positions, next_idx + 1, s_count + is_s)
    current_positions.pop()

    solve(current_positions, next_idx + 1, s_count)


board = []
for _ in range(5):
    row = input().strip()
    board.append(row)

result = 0

solve([], 0, 0)

print(result)