function solution(n, costs) {
    // 1. 비용 기준으로 정렬
    costs.sort((a, b) => a[2] - b[2]);
    
    // 2. 유니온 파인드용 부모 배열
    const parent = Array.from({ length: n }, (_, i) => i);
    
    // 3. find 함수 - 부모 노드 찾기
    function find(x) {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        
        return parent[x];
    }
    
    // 4. union 함수 - 두 집합을 합치기 (사이클이 발생하는지 확인)
    function union(a, b) {
        const rootA = find(a);
        const rootB = find(b);
        if (rootA === rootB) return false;
        parent[rootB] = rootA;
        return true;
    }
    
    // 5. 최소 신장 트리 구성
    let answer = 0;
    for (const [a, b, cost] of costs) {
        if (union(a, b)) {
            answer += cost;
        }
    }
    
    return answer;
}