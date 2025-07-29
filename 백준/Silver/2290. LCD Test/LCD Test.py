import sys

input = sys.stdin.readline


def solve(s, n):
    segment = {
        # 위, 왼위, 오위, 중간, 왼아래, 오아래, 아래
        '0': [1, 1, 1, 0, 1, 1, 1],
        '1': [0, 0, 1, 0, 0, 1, 0],
        '2': [1, 0, 1, 1, 1, 0, 1],
        '3': [1, 0, 1, 1, 0, 1, 1],
        '4': [0, 1, 1, 1, 0, 1, 0],
        '5': [1, 1, 0, 1, 0, 1, 1],
        '6': [1, 1, 0, 1, 1, 1, 1],
        '7': [1, 0, 1, 0, 0, 1, 0],
        '8': [1, 1, 1, 1, 1, 1, 1],
        '9': [1, 1, 1, 1, 0, 1, 1]
    }

    digits = list(str(n))
    rows = ['' for _ in range(2 * s + 3)]

    for idx, digit in enumerate(digits):
        seg = segment[digit]
        line = [''] * (2 * s + 3)

        # 첫째 줄: 위
        line[0] = ' ' + ('-' * s if seg[0] else ' ' * s) + ' '

        # 둘째 줄: 왼위, 오위
        for i in range(1, s+1):
            left = '|' if seg[1] else ' '
            right = '|' if seg[2] else ' '
            line[i] = left + ' ' * s + right

        # 중간 줄:
        line[s + 1] = ' ' + ('-' * s if seg[3] else ' ' * s) + ' '

        # 중간 ~ 마지막 줄 사이: 왼아래, 오아래
        for i in range(s + 2, 2 * s + 2):
            left = '|' if seg[4] else ' '
            right = '|' if seg[5] else ' '
            line[i] = left + ' ' * s + right

        # 마지막 줄
        line[s * 2 + 2] = ' ' + ('-' * s if seg[6] else ' ' * s) + ' '

        # 줄별로 합치기
        for i in range(2 * s + 3):
            rows[i] += line[i]
            if idx != len(digits) - 1:
                rows[i] += ' '

    for row in rows:
        print(row)


s, n = input().split()
solve(int(s), n)
