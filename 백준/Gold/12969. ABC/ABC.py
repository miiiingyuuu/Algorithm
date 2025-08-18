import sys

input = sys.stdin.readline

'''
문자열 S의 길이가 N이고 A, B, C로만 이루어짐
S[i] < S[j]를 만족하는 (i, j) 쌍이 정확히 K개가 되는 경우를 출력 -> A < B < C
ABC로 만들 수 있는 N길이의 조합 중에 위의 조건을 만족하는 경우에 출력하면 될 듯
'''


def solve():
    # dp[pos][a][b][pairs] = pos: 추가할 문자, a: 이전 a의 수, b: 이전 b의 수, pairs: 이전 pairs의 수
    dp = [[[[None] * (K+1) for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0][0] = ("", -1, -1, -1)   # 시작

    for pos in range(N):
        for a in range(N+1):
            for b in range(N+1):
                c = pos - a - b
                if c < 0 or c > N:
                    continue

                for pairs in range(K+1):
                    if dp[pos][a][b][pairs] is None:
                        continue

                    # 다음 문자로 A로 넣는 경우(A를 추가하면 새 쌍 없음)
                    if a+1 < N and dp[pos+1][a+1][b][pairs] is None:
                        dp[pos+1][a+1][b][pairs] = ("A", a, b, pairs)

                    # B 넣는 경우(A와 쌍을 이룸)
                    new_pairs = pairs + a
                    if b+1 < N and new_pairs <= K and dp[pos+1][a][b+1][new_pairs] is None:
                        dp[pos+1][a][b+1][new_pairs] = ("B", a, b, pairs)

                    # C 넣는 경우(A, B와 쌍을 이룸)
                    new_pairs = pairs + a + b
                    if c+1 < N and new_pairs <= K and dp[pos+1][a][b][new_pairs] is None:
                        dp[pos+1][a][b][new_pairs] = ("C", a, b, pairs)

    # 조건을 만족하는 답을 찾기(찾으면 바로 break)
    answer = None
    for a in range(N+1):
        for b in range(N+1):
            c = N - a - b
            if c < 0 or c > N:
                continue

            if dp[N][a][b][K] is not None:
                answer = (a, b, K)
                break

        if answer:
            break

    if not answer:
        return -1

    # 정답 출력
    result = []
    pos, a, b, pairs = N, answer[0], answer[1], answer[2]
    while pos > 0:
        char, pos_a, pos_b, pos_pairs = dp[pos][a][b][pairs]
        result.append(char)
        a, b, pairs = pos_a, pos_b, pos_pairs
        pos -= 1

    return "".join(result[::-1])


N, K = map(int, input().split())

print(solve())
