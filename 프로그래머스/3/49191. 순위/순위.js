function solution(n, results) {
    const graph = Array.from({ length: n + 1 }, () => Array(n + 1).fill(0));
    
    results.forEach(([winner, loser]) => {
        graph[winner][loser] = 1;
        graph[loser][winner] = -1;
    });
    
    // 플로이드 워셜 통해 모든 선수 간의 승패 관계 유추
    // k: 거쳐가는 중간 선수
    for (let k = 1; k <= n; k++) {
        for (let i = 1; i <= n; i ++) {
            for (let j = 1; j <= n; j++) {
                // 만약 i가 k를 이기고, k가 j를 이겼다면, i는 j를 이김
                if (graph[i][k] === 1 && graph[k][j] === 1) {
                    graph[i][j] = 1;
                    graph[j][i] = -1;
                }
            }
        }
    }
    
    // 순위가 확정된 선수는 계산
    let answer = 0;
    for (let i = 1; i <= n; i++) {
        let knowResults = 0;
        for (let j = 1; j <= n; j++) {
            // i와 j의 승패 관계를 안다면 카운트
            if (graph[i][j] !== 0) {
                knowResults++;
            }
        }
        
        // 자기 자신을 제외한 모든 선수와의 관계를 알면 순위 확정
        if (knowResults == n - 1) {
            answer++;
        }
    }
    
    return answer;
}