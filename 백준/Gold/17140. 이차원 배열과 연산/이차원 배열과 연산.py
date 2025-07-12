import sys
from collections import Counter

input = sys.stdin.readline


'''
R 연산: 모든 행에 대해서 정렬 수행 -> 행의 개수 >= 열의 개수인 경우에 적용
C 연산: 모든 열에 대해서 정렬 수행 -> 행의 개수 < 열의 개수인 경우에 적용
정렬은 오름차순인데, 숫자의 수도 오름차순으로(숫자 양이 적은 숫자를 오름차순으로) -> counter 써서 묶은 후에 개수->숫자 크기 순으로 정렬
R연산과 C연산은 사실상 배열을 zip을 통해서 뒤집으면 같은 연산의 함수를 사용하여 해결이 가능
해당하는 열, 행의 값은 하나의 배열 안에 들어가야 하니까 append가 아니고 extend로 해야했다... 디버깅에서 이상한걸 빨리 눈치채야 했다 휴...
'''


def calculate(current_a):
    new_a = []
    max_len = 0

    for row in current_a:
        counter = Counter(num for num in row if num != 0)

        # 해당 숫자들의 양이 작은 숫자들 부터 오름차순 정렬
        sorted_nums = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        new_row = []
        for num, freq in sorted_nums:
            new_row.extend([num, freq])

        # 행 또는 열의 크기가 100을 넘어가면 처음의 100개만 사용
        if len(new_row) > 100:
            new_row = new_row[:100]

        new_a.append(new_row)
        # 연산 후 가장 긴 행의 길이를 통해 빈 자리는 0으로 채우기
        if len(new_row) > max_len:
            max_len = len(new_row)

    for row in new_a:
        row.extend([0] * (max_len - len(row)))

    return new_a


def solve():
    r, c, k = map(int, input().split())  # A[r][c]가 k가 되기 위한 최소 시간
    A = [list(map(int, input().split())) for _ in range(3)]

    time = 0
    # 100초 안에 못찾으면 -1을 반환
    while time <= 100:
        # 답이 나온 순간에 time을 반환
        try:
            if A[r-1][c-1] == k:
                return time
        except IndexError:
            pass

        # 행의 개수가 열의 개수보다 크거나 같으면 R연산, 아니라면 C연산
        if len(A) >= len(A[0]):
            # R연산
            A = calculate(A)
        else:
            # C연산은 해당 배열을 행과 열을 바꾼 후, R연산을 한 후에 다시 원래대로 돌려놓으면 같은 함수로 처리가 가능
            A = list(map(list, zip(*A)))
            A = calculate(A)
            A = list(map(list, zip(*A)))

        time += 1

    return -1


print(solve())
