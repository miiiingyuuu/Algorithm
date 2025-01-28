import sys

input = sys.stdin.readline


def get_bomb_state(current_board, r, c):
    """현재 보드 상태에서 폭발 후의 상태를 계산"""
    next_state = [['O'] * c for _ in range(r)]

    # 폭탄이 있는 위치와 인접 칸들을 '.'으로 변경
    for y in range(r):
        for x in range(c):
            if current_board[y][x] == 'O':
                next_state[y][x] = '.'
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < r and 0 <= nx < c:
                        next_state[ny][nx] = '.'

    return next_state


def print_board(board):
    """보드 상태를 출력"""
    for row in board:
        print(''.join(row))


def main():
    # 입력 처리
    r, c, n = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]

    # n에 따른 상태 처리
    if n <= 1:
        print_board(board)
    elif n % 2 == 0:
        # 짝수 시간에는 모든 칸이 폭탄
        print_board([['O'] * c for _ in range(r)])
    else:
        # 홀수 시간일 때는 n % 4에 따라 다른 상태 출력
        bombs1 = get_bomb_state(board, r, c)  # 첫번째 폭발 상태
        bombs2 = get_bomb_state(bombs1, r, c)  # 두번째 폭발 상태

        if n % 4 == 3:
            print_board(bombs1)
        elif n % 4 == 1:
            print_board(bombs2)


if __name__ == "__main__":
    main()