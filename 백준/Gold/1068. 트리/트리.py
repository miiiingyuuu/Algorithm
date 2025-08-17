import sys

input = sys.stdin.readline


'''
트리를 만든 후에 dfs로 해당 노드를 지웠을때 리프 노드의 갯수 세기(자식이 없다면 리프노드)
'''


def solve(node, children):
    # 삭제된 노드는 없으므로 0 반환
    if node == tar:
        return 0

    # 자식이 없다면 리프노드
    if not children[node]:
        return 1

    cnt = 0
    for child in children[node]:
        cnt += solve(child, children)

    # 모든 자식이 삭제되었다면 자신이 리프노드
    if cnt == 0:
        return 1

    return cnt


N = int(input())
parent = list(map(int, input().split()))
tar = int(input())

# 해당 노드의 자식 노드가 뭐가 있는지 만들기
children = [[] for _ in range(N)]
root = -1

for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        children[parent[i]].append(i)

# tar이 root면 리프노드는 없음
if root == tar:
    print(0)
else:
    print(solve(root, children))
