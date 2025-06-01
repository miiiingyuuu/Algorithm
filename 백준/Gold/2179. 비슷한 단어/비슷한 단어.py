import sys

input = sys.stdin.readline

'''
모든 단어를 비교하면 시간 초과날 가능성 큼
단어들을 사전 순으로 정렬한고, 비슷한 단어들끼리 비교를 하면 시간이 단축 될 듯
접두사의 길이가 최대인 경우가 여러개일 경우에는 순서대로 제일 앞에 있는 단어와 비슷한 단어를 출력
'''


def solve(a, b):
    length = 0
    for x, y in zip(a, b):
        if x == y:
            length += 1
        else:
            break

    return length


n = int(input())
# 입력된 순서의 idx를 기억하기 위한 리스트
words = [(input().strip(), i) for i in range(n)]

# 정렬
words.sort()

max_prefix_len = -1
prefix = ""
ans_min_idx = float('inf')
result = ()

for i in range(n - 1):
    w1, idx1 = words[i]
    w2, idx2 = words[i + 1]
    prefix_len = solve(w1, w2)

    min_idx = min(idx1, idx2)

    # 최대 접두사 길이를 갱신하거나, 같은 길이인데 더 앞선 입력 순서를 가진 경우 갱신
    if prefix_len > max_prefix_len or (prefix_len == max_prefix_len and min_idx < ans_min_idx):
        max_prefix_len = prefix_len
        prefix = w1[:prefix_len]
        ans_min_idx = min_idx
        result = (w1, w2)

# 같은 접두사를 가진 단어들 중 입력 순으로 가장 빠른 2개 찾기
ans = [(w, idx) for w, idx in words if w.startswith(prefix)]
ans.sort(key=lambda x: x[1])

print(ans[0][0])
print(ans[1][0])
