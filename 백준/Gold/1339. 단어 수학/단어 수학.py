import sys

input = sys.stdin.readline


'''
각 단어에 대해 길이 순으로 정렬하면 되지 않을까? 생각했는데, 그렇게 하면 자리 수 마다 큰 숫자를 부여할 수 없음
각 알파벳이 각 자리수에 얼마나 영향을 주는지 가중치 계산, 이 가중치가 가장 큰 문자부터 9 ~ 0까지 숫자 부여
주어진 단어에 그 숫자를 대입해 전체 합을 계산
'''


def solve():
    num = 9
    alpha = {}

    # 9 ~ 0 숫자 부여
    for char, _ in sorted_weights:
        alpha[char] = num
        num -= 1

    # 답 구하기
    ans = 0
    for word in words:
        val = 0
        for char in word:
            val = val * 10 + alpha[char]

        ans += val

    return ans


n = int(input())
words = [list(input().strip()) for _ in range(n)]

# 알파벳 가중치 저장할 dict
weight = {}

# 각 단어의 문자에 대해 가중치 계산
for w in words:
    p = 1
    for c in reversed(w):
        if c in weight:
            weight[c] += p
        else:
            weight[c] = p
        p *= 10

# 가중치 기준으로 내림차순 정렬 (큰 자리 수부터 9 ~ 0을 할당하기 위해)
sorted_weights = sorted(weight.items(), key=lambda x: x[1], reverse=True)

print(solve())
