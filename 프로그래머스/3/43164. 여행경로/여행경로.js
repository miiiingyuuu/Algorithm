function solution(tickets) {
    const graph = {};
    
    // 그래프 구성
    for (const [from, to] of tickets) {
        if (!graph[from]) graph[from] = [];
        graph[from].push(to);
    }
    
    // 목적지를 정렬
    for (const from in graph) {
        graph[from].sort();
    }
    
    const route = ["ICN"]
    const totalTickets = tickets.length;
    
    function solve(current) {
        if (route.length === totalTickets + 1) {
            return true; // 모든 티켓 사용 완료
        }
        
        if (!graph[current] || graph[current].length === 0) {
            return false;   // 해당 지역에서 더 이상 갈 곳 없음
        }
        
        const destinations = graph[current];
        
        for (let i = 0; i < destinations.length; i++) {
            const next = destinations[i];
            
            // 해당 티켓 사용
            destinations.splice(i, 1)
            route.push(next)
            
            if (solve(next)) return true;
            
            // 백트래킹
            route.pop()
            destinations.splice(i, 0, next);
        }
        
        return false;
    }
    
    solve("ICN");
    
    return route;
}