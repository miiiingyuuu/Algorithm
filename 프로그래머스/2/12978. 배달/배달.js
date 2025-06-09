function solution(N, road, K) {
    const graph = Array.from({ length: N + 1 }, () => []);
    
    // 양방향 도로 표시
    for (let [a, b, c] of road) {
        graph[a].push({ to: b, time: c });
        graph[b].push({ to: a, time: c });
    }
    
    const dist = Array(N + 1).fill(Infinity);
    dist[1] = 0;
    
    const pq = [{ node: 1, cost: 0 }];
    
    while (pq.length > 0) {
        // cost가 작은 것 선택(우선순위 큐 같이 사용)
        pq.sort((a, b) => a.cost - b.cost);
        const { node, cost } = pq.shift();
        
        // 이미 더 짧은 경로가 있다면 스킵
        if (cost > dist[node]) continue;
        
        for (let neighbor of graph[node]) {
            const nextCost = cost + neighbor.time;
            
            if (nextCost < dist[neighbor.to]) {
                dist[neighbor.to] = nextCost;
                pq.push({ node: neighbor.to, cost: nextCost });
            }
        }
    }
    
    // K 시간 이하로 배달 가능한 마을 수 세기
    return dist.filter(time => time <= K).length;
}