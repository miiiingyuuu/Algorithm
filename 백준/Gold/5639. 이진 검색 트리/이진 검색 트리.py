import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def make_postorder(preorder, start, end):
    if start > end:
        return
        
    root = preorder[start]  # 현재 서브트리의 루트
    
    # 루트보다 큰 첫 번째 값의 인덱스를 찾음 (오른쪽 서브트리의 시작)
    right_start = start + 1
    while right_start <= end and preorder[right_start] < root:
        right_start += 1
    
    # 왼쪽 서브트리 순회 (start+1 ~ right_start-1)
    make_postorder(preorder, start + 1, right_start - 1)
    
    # 오른쪽 서브트리 순회 (right_start ~ end)
    make_postorder(preorder, right_start, end)
    
    # 현재 노드 출력
    print(root)

# 입력 받기
preorder = []
while True:
    try:
        num = input().strip()
        if num == '':
            break
        preorder.append(int(num))
    except:
        break

# 후위 순회 결과 출력
make_postorder(preorder, 0, len(preorder) - 1)