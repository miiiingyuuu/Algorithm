function solution(n, roads, sources, destination) {
    const graph = Array.from({ length: n + 1 }, () => []);
    
    for (const [a, b] of roads) {
        graph[a].push(b);
        graph[b].push(a);
    }
    
    // destinations에서 모든 지역까지의 최단거리를 bfs로 계산
    const distances = new Array(n + 1).fill(-1);
    const queue = [destination];
    distances[destination] = 0;
    
    while (queue.length > 0) {
        const current = queue.shift();
        
        for (const neighbor of graph[current]) {
            if (distances[neighbor] === -1) {
                distances[neighbor] = distances[current] + 1;
                queue.push(neighbor);
            }
        }
    }
    
    // 각 source에서 destinatin까지의 거리 반환
    return sources.map(source => distances[source]);
}