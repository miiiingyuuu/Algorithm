function solution(n, wires) {
    let answer = n;
    
    // bfs로 연결된 송전탑 개수 세기
    function bfs(start, graph, visited) {
        let count = 1;
        let queue = [start];
        visited[start] = true;
        
        while (queue.length > 0) {
            const node = queue.shift();
            for (let next of graph[node]) {
                if (!visited[next]) {
                    visited[next] = true;
                    queue.push(next);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    // 모든 간선을 하나씩 끊어보면서 차이 계산
    for (let i = 0; i < wires.length; i++) {
        const graph = Array.from({ length: n + 1 }, () => []);
        
        // 간선 하나 제거
        for (let j = 0; j < wires.length; j++) {
            if (i === j) continue;
            const [a, b] = wires[j];
            graph[a].push(b);
            graph[b].push(a);
        }
        
        const visited = Array(n + 1).fill(false);
        const count = bfs(1, graph, visited);
        const diff = Math.abs(n - count - count);
        answer = Math.min(answer, diff);
    }
    
    return answer;
}