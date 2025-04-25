import sys
from collections import deque
input = sys.stdin.readline


def insert(path, trie):
    node = trie
    for i in path:
        if i not in node:
            node[i] = {}    # 새로운 방이 없으면 새 딕셔너리로 추가
        node = node[i]      # 다음 층으로 이동


def solve(node, depth):
    for key in sorted(node.keys()):
        print("--" * depth + key)
        solve(node[key], depth + 1)


n = int(input())
trie = {}

for _ in range(n):
    parts = input().split()
    k = int(parts[0])
    path = parts[1:]
    insert(path, trie)

solve(trie, 0)