import sys

input = sys.stdin.readline

'''
소수가 연속되어야지만 해당 하는 값을 얻을 수 있음
근데 해당 소수 다음의 숫자가 소수인걸 어떻게 알 수 있을까? -> 에라토스테네스의 체로 소수 리스트를 얻고
투포인터를 통해서 연속된 소수로 n을 얻을 수 있는지 체크
'''


def solve():
    # 에라토스테네스의 체를 이용하여 n 이하의 소수를 구하기
    def get_primes(n):
        board = [True] * (n + 1)
        board[0] = board[1] = False
        for i in range(2, int(n**0.5) + 1):
            if board[i]:
                for j in range(i*i, n + 1, i):
                    board[j] = False

        return [i for i, is_prime in enumerate(board) if is_prime]

    primes = get_primes(n)

    cnt = 0
    left = 0
    right = 0
    cur_sum = 0

    while True:
        if cur_sum >= n:
            if cur_sum == n:
                cnt += 1
            cur_sum -= primes[left]
            left += 1
        elif right == len(primes):
            break
        else:
            cur_sum += primes[right]
            right += 1

    return cnt


n = int(input())

print(solve())
